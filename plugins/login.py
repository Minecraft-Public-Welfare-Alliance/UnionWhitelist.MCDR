from mcdreforged.api.command import *
from mcdreforged.command.command_source import CommandSource
from mcdreforged.info_reactor.info import Info
from mcdreforged.minecraft.rcon.rcon_connection import RconConnection
from threading import Thread
import time
import requests
import json
import os
PLUGIN_METADATA = {
    'id': 'unionWhitelist',
    'version': '1.0.0',
    'name': 'login',
    'description': 'MPWA联盟验证mcdr端',
    'author': 'ZQHD',
    'link': 'https://github.com',

}
jsonFile = open('setting.json', "r")
json = json.load(jsonFile)
rconSetting = json['rcon']
rcon = RconConnection(rconSetting['address'], rconSetting['port'], rconSetting['password'])
userKeys = ""
serverName = ""
accountName = ""
password = ""

def on_load(server, old):
    buider = SimpleCommandBuilder()
    buider.command("!!mpwa ban <name> <description>", ban)  # 永封
    buider.command("!!mpwa prosecute <level> <description>", prosecute)  # 处罚
    buider.arg("name", Text)
    buider.arg("description", Text)
    buider.arg("level", Integer)
    server.logger.info('load is successful')
    buider.register(server)
    setting = json['setting']
    serverName = setting['serverName']
    accountName = setting['accountName']
    password = setting['password']
    # response = requests.get("https://www.mpwa.cn/McServerSig",headers={
    #     "sname":serverName,
    #     "lname":accountName,
    #     "lpwd":password
    # })
    # userKeys = response.text
    thread = Thread(target=loop)
    thread.start()
def on_user_info(server, info:Info):
    if info.content == 'mpwa bind':
        user = info.player
        timeNow = time.time()
        server.reply(info, '绑定开始！用户名：{}，时间：{}'.format(user, time.strftime("%Y.%m.%d %h:%n:%s")))


def ban(source: CommandSource, context: CommandContext):
    name = context['name']
    description = context['description']
    # Todo : 请求接口，推送黑名单


def prosecute(source: CommandSource, context: CommandContext):
    level = context['level']
    description = ['description']


def on_server_stop(server, server_return_code: int):
    json.close()


def loop():
    """
    循环执行部分的代码，如请求接口
    :return:
    """
    while True:
        # todo:编写请求白名单黑名单的接口
        newWhitelist = []  # 新白名单表单
        newBanList = []  # 新黑名单表单
        for whitelist in newWhitelist:
            rcon.send_command("whitelist add {}".format(whitelist))
        for banList in newBanList:
            rcon.send_command("ban {}".format(banList))
        time.sleep(300)
