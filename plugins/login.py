from mcdreforged.api.command import SimpleCommandBuilder
from mcdreforged.info_reactor.info import Info
from mcdreforged.minecraft.rcon.rcon_connection import RconConnection
import time
PLUGIN_METADATA = {
    'id': 'login',
    'version': '1.0.0',
    'name': 'My Plugin',
    'description': 'MPWA联盟验证mcdr端',
    'author': 'ZQHD',
    'link': 'https://github.com',

}
rcon = RconConnection("127.0.0.123",38324,"123456")
def on_load(server, old):
    buider = SimpleCommandBuilder()
    # buider.command("mpwa bind",bind)
    server.logger.info('Hello world!')
    buider.register(server)
def on_user_info(server, info:Info):
    if info.content == 'mpwa bind':
        user = info.player
        server.reply(info, '绑定开始！用户名：{}，时间：{}'.format(user,time.time()))
# def bind():
#     print("succeed")
