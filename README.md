# Educg Fake - 希冀考试程序设备信息代理

[![](https://img.shields.io/github/license/inkdust2021/educg_fake)](LICENSE)

由于希冀的考试程序只能在Windows使用，而我的设备是mac，为了让我可以正常考试，于是便有了这个程序，这个程序可以让你可以让你正常访问互联网的情况下让希冀考试页面认为你打开了考试程序。

## 免责声明

**本组织和个人不接受任何资金捐助和交易，此项目是纯粹研究交流学习性质！**

## 功能说明

该程序提供以下功能：

1. **设备信息代理**：拦截并缓存考试程序的网络适配器和设备信息
2. **CORS 支持**：允许跨域访问 API 端点

## API 端点

- `GET /` - 欢迎页面
- `GET /GetAdapterInfo` - 返回网络适配器信息（JSON 格式）
- `GET /GetDeviceInfo` - 返回设备信息（JSON 格式）

## 使用方法

### 基本模式

```bash
python educg_fake.py
```

运行流程：

1. 打开考试程序

2. 按下回车，程序将从考试程序获取真实设备信息

3. 关闭考试程序

4. 按下回车，代理服务器将在 `http://127.0.0.1:8087` 启动

5. 程序将使用缓存的设备信息响应后续请求

   （其实程序本来是写死在里面一套设备信息的，但是为了开源，被我去掉了）

## 系统要求

- Python 3.x
- Flask 库

安装依赖：

```bash
pip install flask
```

## 注意事项

- 服务器运行在本地 `127.0.0.1:8087` 端口
- 程序需要先从真实考试程序获取设备信息，然后才能作为代理运行
- 使用 Ctrl+C 可以停止服务器

## 工作原理

1. 希冀的考试程序运行原理为在本地运行api服务器，并将考试信息与设备信息分别放到`/GetAdapterInfo` 和 `/GetDeviceInfo`端点
2. 程序首先从运行中的考试程序获取 `/GetAdapterInfo` 和 `/GetDeviceInfo` 的真实响应
3. 将这些响应缓存在内存中
4. 启动本地 Flask 服务器，监听相同端口
5. 后续请求直接返回缓存的设备信息，无需真实考试程序运行

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=inkdust2021/educg_fake&type=date&legend=top-left)](https://www.star-history.com/#inkdust2021/educg_fake&type=date&legend=top-left)

