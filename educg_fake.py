from flask import Flask, Response
import urllib.request
import sys

app = Flask(__name__)
ADAPTER_RAW = None
DEVICE_RAW = None


def fetch_from_real_program():
    try:
        with urllib.request.urlopen('http://127.0.0.1:8087/GetAdapterInfo', timeout=5) as response:
            adapter_raw = response.read()
        with urllib.request.urlopen('http://127.0.0.1:8087/GetDeviceInfo', timeout=5) as response:
            device_raw = response.read()
        return adapter_raw, device_raw
    except Exception:
        return None, None


@app.route('/')
def index():
    return Response("Welcome to tinyweb", mimetype='text/html')


@app.route('/GetAdapterInfo')
def get_adapter_info():
    response = Response(ADAPTER_RAW, mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/GetDeviceInfo')
def get_device_info():
    response = Response(DEVICE_RAW, mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.errorhandler(404)
def handle_404(e):
    return Response("<h3>404 Page Not Found<h3>", mimetype='text/html', status=404)


def main():
    global ADAPTER_RAW, DEVICE_RAW
    print("打开考试程序，按下回车开始运行")
    try:
        input()
    except EOFError:
        pass
    adapter_raw, device_raw = fetch_from_real_program()
    if not adapter_raw or not device_raw:
        sys.exit("无法获取真实程序数据")
    ADAPTER_RAW = adapter_raw
    DEVICE_RAW = device_raw
    print("获取数据完毕，请关闭考试程序并按下回车开始运行")
    try:
        input()
    except EOFError:
        pass
    print("服务启动: http://127.0.0.1:8087")
    app.run(host='127.0.0.1', port=8087, debug=False)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("服务已停止")
    except Exception as e:
        print(f"错误: {e}")
