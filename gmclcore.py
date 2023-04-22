from datetime import datetime
from json import dumps, loads
from os import getcwd, mkdir, remove, system
from os.path import isdir, isfile
from time import mktime
from zipfile import ZipFile


def unzip(filename, path) -> None:
    with ZipFile(filename) as zipfile:
        for z in zipfile.namelist():
            zipfile.extract(z, path)


def run(mcdir, version, java_path, max_men, mc_args="") -> None:
    class_path = ""

    version_json = open(mcdir + "/versions/" + version +
                        "/" + version + ".json", "r")
    dic = loads(version_json.read())
    for lib in dic["libraries"]:
        if "rules" in lib:
            if lib["rules"][0]["os"]["name"] == "windows":
                dirct_path = mcdir + "/versions/" + version + \
                    "/" + version + "-natives"  # 解压到的目标路径
                filepath = mcdir + "/libraries/" + \
                    lib["downloads"]["artifact"]['path']  # 要解压的artifect库
                unzip(filepath, dirct_path)
        elif "rules" not in lib:
            dirct_path = mcdir + "\\versions\\" + version + \
                "\\" + version + "-natives"  # 解压到的目标路径
            filepath = mcdir + "/libraries/" + \
                lib["downloads"]["artifact"]['path']  # 要解压的artifect库
            unzip(filepath, dirct_path)
    jvm = '"' + java_path + '" -XX:+UseG1GC -XX:-UseAdaptiveSizePolicy' + \
          ' -XX:-OmitStackTraceInFastThrow -Dfml.ignoreInvalidMinecraftCertificates=True ' + \
          '-Dfml.ignorePatchDiscrepancies=True -Dlog4j2.formatMsgNoLookups=true ' + \
          '-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump ' + \
          '-Dos.name="Windows 10" -Dos.version=10.0 -Djava.library.path="' + \
          mcdir + "/versions/" + version + "/" + version + "-natives" + \
          '" -Dminecraft.launcher.brand=launcher ' + \
          '-Dminecraft.launcher.version=1.0.0 -cp'
    class_path += '"'  # 这一句我在教程里面写错了，应该填加在这里，让-cp以引号开头
    for lib in dic["libraries"]:
        if "rules" not in lib.keys():
            normal = mcdir + "/libraries/" + \
                lib["downloads"]["artifact"]["path"]  # 普通库路径
            class_path += normal + ";"  # 将普通库路径追加到-cp后面
    # 将客户端文件传入-cp参数
    class_path = class_path + mcdir + "/versions/" + \
        version + "/" + version + ".jar" + '"'
    # 设置最大运行内存
    jvm = jvm + " " + class_path + " -Xmx" + max_men + \
        " -Xmn256m -Dlog4j.formatMsgNoLookups=true"
    # 最大内存由变量maxMen决定,最小内存是256M

    # 配置Minecraft参数
    # 将主类传入Minecraft参数
    mc_args += dic["mainClass"] + " "
    for arg in dic["arguments"]["game"]:
        if isinstance(arg, str):
            mc_args += arg + " "
        elif isinstance(arg, dict):  # 无论是什么，只要是在大括号里括着的，都被python认为是字典类型
            if isinstance(arg["value"], list):
                for a in arg["value"]:
                    mc_args += a + " "
            elif isinstance(arg["value"], str):
                mc_args += arg["value"] + " "
    # 将模板替换为具体数值
    mc_args = mc_args.replace("${auth_player_name}", "username")  # 玩家名称
    mc_args = mc_args.replace("${version_name}", version)  # 版本名称
    mc_args = mc_args.replace("${game_directory}", mcdir)  # mc路径
    mc_args = mc_args.replace("${assets_root}", mcdir + "/assets")  # 资源文件路径
    mc_args = mc_args.replace(
        "${assets_index_name}", dic["assetIndex"]["id"])  # 资源索引文件名称
    mc_args = mc_args.replace(
        "${auth_uuid}", "1af421541e743fa180f63f010131cefb")  # 由于没有写微软登录,所以uuid为空的
    mc_args = mc_args.replace(
        "${auth_access_token}", "a8dfb29215624befa9b46f0c6330f3f5")  # 同上
    mc_args = mc_args.replace("${clientid}", version)  # 客户端id
    mc_args = mc_args.replace("${auth_xuid}", "{}")  # 离线登录,不填
    mc_args = mc_args.replace("${user_type}", "legacy")  # 用户类型,离线模式是Legacy
    mc_args = mc_args.replace("${version_type}", dic["type"])  # 版本类型
    mc_args = mc_args.replace("${resolution_width}", "872")  # 窗口宽度
    mc_args = mc_args.replace("${resolution_height}", "498")  # 窗口高度
    mc_args = mc_args.replace("-demo ", "")  # 去掉-demo参数，退出试玩版
    # 组装命令条
    command_line = jvm + " " + mc_args
    print(command_line)
    # 使用bat的方法运行过长的命令条
    with open("run.bat", "w") as bat:
        bat.write(command_line)
    system("run.bat")
    # 视频中没有讲到的,在运行完Minecraft之后，删除run.bat，这样可以避免与其他文件冲突(如果真有人写了一个运行py文件的.bat文件，名字叫run.bat的话,别问我怎么知道的)
    remove("run.bat")


class Config:
    def __init__(self) -> None:
        self.config = {}
        self.examples = {
            "game_dir": "",
            "java_path": "",
        }
        if isfile("gmcl.json"):
            self.refresh()
        else:
            self.write(self.examples)
            self.refresh()

    def get(self, str):
        return self.config[str]

    def save(self, op, str) -> None:
        self.config[op] = str
        self.write(self.config)

    def write(self, dict) -> None:
        with open("gmcl.json", "w") as config:
            config.write(dumps(dict, ensure_ascii=False,
                         sort_keys=True, indent=4, separators=(',', ': ')))

    def refresh(self) -> None:
        with open("gmcl.json", "r") as c:
            self.config = loads(c.read())


if __name__ == '__main__':
    pass
