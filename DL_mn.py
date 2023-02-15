#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Description:TikTok.py
@Date       :2023/01/27 19:36:18
@Author     :imgyh
@version    :1.0
@Github     :https://github.com/imgyh
@Mail       :admin@imgyh.com
-------------------------------------------------
Change Log  :
-------------------------------------------------
'''

import argparse
import json
import os

from TikTok import TikTok


def ld(link, path):
    dic = dict(
        link=link,
        path=path,
        music=True,
        cover=True,
        avatar=True,
        mode="like",
    )
    args = argparse.Namespace(**dic)
    tk = TikTok()
    url = tk.getShareLink(args.link)
    key_type, key = tk.getKey(url)
    if key is None or key_type is None:
        return
    elif key_type == "user":
        datalist = tk.getUserInfo(key, args.mode, 35)
        tk.userDownload(awemeList=datalist, music=args.music, cover=args.cover, avatar=args.avatar,
                        savePath=args.path)
    elif key_type == "aweme":
        datanew, dataraw = tk.getAwemeInfo(key)
        tk.awemeDownload(awemeDict=datanew, music=args.music, cover=args.cover, avatar=args.avatar,
                         savePath=args.path)
    elif key_type == "live":
        live_json = tk.getLiveInfo(key)
        if not os.path.exists(args.path):
            os.mkdir(args.path)

        # 保存获取到json
        print("[  提示  ]:正在保存获取到的信息到result.json\r\n")
        with open(os.path.join(args.path, "result.json"), "w", encoding='utf-8') as f:
            f.write(json.dumps(live_json, ensure_ascii=False, indent=2))
            f.close()


def main():
    mn_list = ["https://v.douyin.com/BV7Em38/", ]
    mc_list = ["https://v.douyin.com/BVvttcD/", ]
    gx_list = [ ]
    for link in mn_list:
        path = "./dl/mn/"
        ld(link,path)
    for link in mc_list:
        path = "./dl/mc/"
        ld(link,path)
    for link in gx_list:
        path = "./dl/gx/"
        ld(link,path)


if __name__ == "__main__":
    main()
