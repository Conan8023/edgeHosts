import os, re

hosts = r'C:\Windows\System32\drivers\etc\hosts'


# 若hosts未写入过相关代码，就在末尾追加
def write_dns():
    getIP = input("请输入你查询到的IP地址：")
    dns = '\n' + getIP + ' edge.microsoft.com #Edge翻译\n' \
          + getIP + ' msedgeextensions.sf.tlu.dl.delivery.mp.microsoft.com #Edge商店扩展'

    with open(hosts, 'a',encoding='utf-8') as tmp:
        tmp.write(dns)
        print(dns + '\n写入成功!')
        tmp.close()


# 若hosts写入过相关代码，就在修改ip地址
def change_dns():
    getIP = input("请输入你查询到的IP地址：")
    a1 = getIP + ' edge.microsoft.com #Edge翻译'
    a2 = getIP + ' msedgeextensions.sf.tlu.dl.delivery.mp.microsoft.com #Edge商店扩展'
    with open(hosts, 'r', encoding='utf-8') as readhost:
        lines = readhost.read()
        s = re.sub('(.*?) edge.microsoft.com #Edge翻译', a1, lines)
        b = re.sub('(.*?) msedgeextensions.sf.tlu.dl.delivery.mp.microsoft.com #Edge商店扩展', a2, s)
        readhost.close()
    print('\n您的hosts文件内容：' + b)
    with open(hosts, 'w', encoding='utf-8') as f2:
        f2.write(b)
        f2.close()
    print("已修改完成！")


# 主函数，判断hosts是否被写入过相关代码
def main():
    with open(hosts, 'r', encoding='utf-8') as f0:
        f1 = f0.read()
        a = 'edge.microsoft.com'
        if a in f1:
            change_dns()
        else:
            write_dns()
        f0.close()
    os.system('ipconfig /flushdns') # 调用cmd系统命令，刷新dns缓存
    print('\n')
    os.system('pause')              # cmd命令，按任意键退出


if __name__ == '__main__':
    # os.system('explorer http://ping.chinaz.com/microsoftedge.microsoft.com')
    print('使用说明：\n\t1.右键以管理员身份运行该程序，如若双击打开，请退出以管理员身份再次运行！\n'
          '\t2.在浏览器中打开：http://ping.chinaz.com/microsoftedge.microsoft.com\n'
          '\t  复制下方得到的ip地址，例如：13.107.6.158，将其复制粘贴到本程序下方输入位置，然后回车即可！\n'
          '\t  本程序会自动填写hosts文件内容，并自动刷新DNS缓存！\n'
          '\t3.若曾在hosts文件内填写过edge.microsoft.com相关代码（姑且称之为代码^_^），程序会自动修改其ip地址！\n'
          '\t  若没有，则程序会在hosts文件末尾追加上相关代码！\n'
          '\t4.本程序会在你电脑没有hosts文件时，自动创建hosts文件，路径：C:\Windows\System32\drivers\etc\hosts\n'
          '\t5.根据知乎博主：红尘 的文章教程制作的程序，文章地址：https://zhuanlan.zhihu.com/p/473437761\n'
          '\t6.保守起见，还请先自行备份hosts文件！\n'
          '\t7.项目开源地址：https://gitee.com/conan8023/edge-hosts\n'
          '\t8.使用方法视频版演示教程以及问题反馈地址：\n'
          '\t9.程序作者：哔哩哔哩UP主：阿哲-啊这\n')
    if not os.path.exists(hosts):
        os.system('type nul>C:\Windows\System32\drivers\etc\hosts')  # 调用系统命令来创建hosts文件
    main()
