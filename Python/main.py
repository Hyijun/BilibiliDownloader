import time
import requests as req


def add_common_info(info):
    now_time = time.strftime('%H:%M:%S /', time.localtime(time.time()))
    print('[' + now_time + 'INFO] ' + info)


# 获得HTML
def get_bilibili_html(av_url):
    # 设置头文件，应对反爬措施
    bilibili_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Cookie': 'buvid3=1F524FE2-8022-4945-A0AF-62ECB45FAD6E163017infoc; LIVE_BUVID=AUTO7215339028787612; '
                  ' im_notify_type_1=1',
        'Host': 'www.bilibili.com'
    }

    # 直接返回HTML代码
    return req.get(av_url, headers=bilibili_headers).text


# 通过find方法找到视频下载链接
def get_download_url(video_url_html):
    # find这个URL开头
    video_url_html = video_url_html[video_url_html.find('http://upos-hz-mirrorcos.acgvideo.com/'):]
    # find结尾
    return video_url_html[:video_url_html.find('"]')]


# 下载器，单线程
def download_bilibili_video(bilibili_url, video_url):
    # 同样要头文件
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Referer': video_url,   # 需要视频链接
        'Origin': 'https://www.bilibili.com'
    }
    return req.get(bilibili_url, headers=header).content     # 返回数据流


def get_video_name(bilibili_html):
    start = bilibili_html.find('<title data-vue-meta="true">') + 28
    bilibili_html = bilibili_html[start:]
    return bilibili_html[:bilibili_html.find('_哔哩哔哩 ')]


def main():
    print('\t欢迎使用：当前程序处于测试阶段\n\t版本号[alpha 1.0.0]')
    print('############################################################')
    add_common_info('程序开始运行')
    video_url = 'https://www.bilibili.com/video/' + input('请输入AV号')
    file_name = input('请输入想要命名的文件名')
    add_common_info('正在获取视频')
    file = download_bilibili_video(get_download_url(get_bilibili_html(video_url)), video_url)
    add_common_info('视频获取成功')
    with open(file_name, 'wb') as f:
        add_common_info('开始写入文件')
        f.write(file)
    add_common_info('写入成功')
    add_common_info('程序成功执行')


if __name__ == '__main__':
    # main()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Cookie': 'buvid3=1F524FE2-8022-4945-A0AF-62ECB45FAD6E163017infoc; LIVE_BUVID=AUTO7215339028787612; '
                  ' im_notify_type_1=1',
        'Host': 'www.bilibili.com'
    }
    url = 'https://www.bilibili.com/video/' + input('请输入AV号')
    print('一')
    html = req.get(url, headers=headers).text
    print(html)
    print('######################################################################')
    print(get_video_name(html))
    print('end')
    time.sleep(1000)
