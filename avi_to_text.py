# -*- encoding: utf-8 -*-
"""
@File    :   ui.py
@Time    :   2021年04月02日 21:19:56 星期五
@Author  :   erma0
@Version :   1.0
@Link    :   https://erma0.cn
@Desc    :   UI界面
"""
import json
import webview

from transer_api import RequestApi


class API:
    """
    前后端交互接口
    """

    def __init__(self):
        """
        初始化
        """
        self.res = ''
        self.target = ''
        self.appid = ''
        self.secret_key = ''
        try:
            with open('D:/result.txt', 'r') as load_f:
                load_dict = json.load(load_f)
                self.appid = load_dict["appid"]
                self.secret_key = load_dict['appsecret']
        except:
            self.appid = ''
            self.secret_key = ''

    def start_transfer(self, target):
        self.target = target

        if not self.appid or not self.secret_key:
            window.evaluate_js('app.starterror()')
            return
        if not target:
            window.evaluate_js('app.openError();')
            return
        window.evaluate_js('app.loading=true;')
        try:
            print(self.appid)
            print(self.secret_key)
            api = RequestApi(appid=self.appid, secret_key=self.secret_key,
                             upload_file_path=target)
            taskid = api.all_api_request()
            if taskid == '错误':
                print('cuowu')
                self.res = '音频解析错误，请重新上传'
                window.evaluate_js('app.setData();app.loading=false;app.transferError();')
                return
            res = api.finall_result(taskid)
            self.res = res
            window.evaluate_js('app.setData();app.loading=false;app.openSuccess();')
        except:
            window.evaluate_js('app.starterror()')

    def return_data(self):
        return self.res

    def apiconfiguration(self, appid, appsecret):
        self.appid = appid
        self.secret_key = appsecret
        result = {'appid': appid,
                  'appsecret': appsecret}
        # 以json格式写入文件
        with open("D:/result.txt", "w") as fp:
            fp.write(json.dumps(result, indent=4, ensure_ascii=False))
        print(self.appid)
        print(self.secret_key)
        print('saf')

    def stop_search(self):
        if not self.target:
            window.evaluate_js('app.openError();')
        window.evaluate_js('app.loading=false;')
        print('停止采集---')

    def register(self):
        try:
            # res = requests.get("xxx")
            # respose = res.json()
            respose = {'code': 200}
            if respose['code'] == 200:
                return 200
            else:
                return 300
        except Exception as e:
            print(e)
            return 300

    def openFile(self):
        # print('py', "打开文件")*.mp3 * wav * flac * m4a * opus
        file_types = ('音频文件(*.mp3;*.wav;*.flac;*.m4a;*.opus)', '全部文件 (*.*)')
        result = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=False, file_types=file_types)
        print('py 打开文件', result)
        return result[0]


if __name__ == "__main__":
    api = API()
    chinese = {
        'global.quitConfirmation': u'确定要关闭吗?',
    }
    window = webview.create_window(
        title='音频转换文本工具',  # 标题
        url='static/index.html',  # 本地文件或网络URL
        js_api=api,  # 暴露api对象，或使用flask等服务创建的对象
        width=890,  # 窗口宽；好像和网页中大小不一样，网页中大小为620*470px
        height=620,  # 窗口高
        resizable=False,  # 是否可以缩放窗口
        frameless=False,  # 窗口是否无边框
        confirm_close=True,  # 退出确认
        transparent=False
    )
    webview.start(debug=True, localization=chinese)
