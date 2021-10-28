# SubAndSeasonFilesRename

剧集与字幕批量改名

![image](https://github.com/Reboot93/SubAndSeasonFilesRename/raw/master/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202021-10-24%20235401.jpg)
![image](https://github.com/Reboot93/SubAndSeasonFilesRename/raw/master/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202021-10-24%20235410.jpg)

v1.0.1 不支持同时修改不同文件夹的文件

支持添加季与集信息的剧集格式：

    xxxxxx(r' [0-9]{1,4} ')xxxxxx.xxx

    xxxxxx(r'【[0-9]+[v[0-9]{1,3}[A-Z]{0,4}]?[OVA]?】')xxxxxxx.xxx

    xxxxxx(r'\[[0-9]+[v[0-9]{1,3}[A-Z]{0,4}]?[OVA]?\]')xxxxxx.xxx

    xxxxxx(r'EP[0-9]+')xxxxxxxxxx.xxx

在v1.0.1中增加了自定义用于识别集数的正则表达式的功能：

    例如：
        文件名：new[【12】].mkv
        在界面中输入正则表达式：\[【[0-9]+】\]
        并指定数字起始位 [ 【 1 2 】 ]
        对应位数         1 2 3
        起始位为第3位