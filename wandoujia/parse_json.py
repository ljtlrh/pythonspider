# -*- coding=utf-8 -*-

import pandas as pd

__author__ = 'STM'

if __name__ == '__main__':
    name = {'影音播放': ['哔哩哔哩', 'PP体育', '酷狗音乐', '搜狐视频', '腾讯视频', '优酷视频', '火山小视频', '迅雷', '网易云音乐', '西瓜视频', '影音先锋', '搞笑斗图大师',
                     '全民K歌', 'QQ音乐', '虎牙直播', '触手直播', '美女VR视频', 'PP视频', '咪咕音乐', '万能视频播放器', '芒果TV', '免费影音看片', '酷我音乐',
                     '好看视频', '咪咕视频', '影视大全', '橙色VR影视', '深夜直播', '斗鱼直播', '铃声多多', '虾米音乐', '皮皮虾', '360影视大全', '爱奇艺PPS', '快猫',
                     'YY', 'YouTube', '影视大全', '暴风影音', '花椒直播', '唱吧', '乐视视频', '咪咕圈圈', '土豆视频', '手机电视', '蜜秀直播', '优艺直播',
                     '桃花直播', '影视大全纯净版', '西瓜影音', '建筑工程准题库', '九秀美女直播', '聊客', '央视影音', '水多直播', '猫咪视频直播', '小寡妇', '韩剧TV',
                     '么么直播', '企鹅电竞', '人人视频', '直播吧', '美女直播间', '免费影视', '手机万能播放器', '熊猫直播', '吉吉影音', '快狐', '腾讯视频HD', '映客',
                     '两个微信', '超级看影院', '糖豆', 'PP体育', '波波视频', '听多多', 'VR在线', '快手看片', '优酷电视助手', '电视家', '速播影视', '超级视频',
                     '不要虐待美女（欧美-美女花园）', '萤石云视频', '午夜被窝看片神器', 'Biu视频桌面', '蜜蜜直播', '秀吧直播', '百度视频', '爱奇艺TV', '微色', '手机看片神器',
                     '六间房秀场', 'Koznak', '全网影视大全', '万能影视', '小草莓直播', '光环助手', '种子视频', '影视大全高清版', '一直播', '视频播放器',
                     'MoboPlayer', '手机电视直播', '酷狗直播', '红人直播', '酷狗铃声', '酷我音乐HD', '石榴直播', '1905电影网', 'MX Player', '全民K诗',
                     '手机收音机', '手机来电铃声', '宅男宝贝', '先锋影视播放器', '迅雷影音(云播)', '羚萌直播', '手机电视直播大全', '桃色熟女'],
            '系统工具': ['搜狗浏览器', '360浏览器', '钱盾', '腾讯WiFi管家', 'WiFi万能钥匙', '百度极速版', '百度', 'UC浏览器', '猎豹清理大师', '清理大师',
                     '360手机卫士', '搜狗输入法', 'UC浏览器福利版', 'QQ浏览器', '腾讯手机管家', '谷歌浏览器Google Chrome', '豌豆荚', 'KingRoot',
                     'Google空间', '星球联盟', '讯飞输入法', '网易UU加速器', '无线密码破解器', '手机管家', '\xa0趣输入', 'WIFI密码查看器', '搜狗搜索',
                     '谷歌服务框架及谷歌商店安装神器', '360浏览器', 'WiFi密码查看工具', 'WiFi密码查看神器', '存储空间清理', 'WiFi信号增强器', '游戏超人',
                     '\xa0360清理大师', '互传', '百度输入法', 'Google Play 服务', '一键ROOT大师', 'PP助手', 'QQ安全中心', '浏览器', '360超级ROOT',
                     'BT磁力种子搜索神器', '2345浏览器', '3733游戏盒', '夸克浏览器', '双开助手微信多开分身版', '谷歌安装器', 'ROOT大师', '百度手机卫士', 'GO谷歌安装器',
                     'ES文件浏览器', '7724游戏盒', '万能WiFi钥匙', '手机乐园', '微信自动抢红包', '谷歌安装器', '手机数据恢复精灵', 'ROOT精灵', '天天清理',
                     '百度一键root', '刷机精灵', '超级清理大师', 'Firefox火狐浏览器', '闪电盒子', '豹来电', '安兔兔评测', '小鸡模拟器', 'RE文件管理器',
                     'ZArchiver 解压缩工具', '2345手机助手', '爱吾游戏助手', 'QQ浏览器Play版', 'TP-LINK', '鲁大师评测', 'Uyghurche Kirguzguch',
                     '猎豹浏览器', '烧饼修改工具', '智代还', '微痕迹', '按键精灵', '掌心输入法', 'QQ输入法', '天气派', '换机助手', '茄子快传', '金山电池医生', '米家',
                     '投屏神器', '百度浏览器', 'KK键盘', 'WiFi 连网神器', 'Flash播放器设置', '微粉管家', '私密浏览器', '谷歌服务框架', '变声器', '手机快速充电',
                     'MM应用商场', '室内温度计', '谷歌安装器', '红手指云手机', 'lbe安全大师', '闪传', 'Chrome浏览器测试版', '刷机大师', '360免费WiFi',
                     'Xposed框架', '小米路由器', 'otkax', 'Adobe AIR', 'Google身份验证器 Google Authenticator'],
            '通讯社交': ['MOMO陌陌', '挖客', '微信', 'QQ', '皖事通', '花间', '探探', '捞月狗', '微博', '微信聊天记录恢复', 'QQ轻聊版', '脉脉', '配配',
                     '万能表情', '百度贴吧', '桌趣', '恋爱漂流瓶', '秀色直播', '派派', '比心', 'QQ同步助手', '微博国际版', '附近语聊约会', '美媛直播', '淘色直播',
                     '迷你世界助手盒子', '天天短信群发', 'Blued', '音遇', '闲聊', '同桌游戏', '18游戏盒', '小鹿情感', '云尚佳人', '连信', '奥豆', 'QQ国际版',
                     '缘约交友', '富聊一对一视频', '明日之后助手', '最右', '微信表情大全', '陪聊迷音遇见你', 'QQ空间', '播聊同城视频约', '密聊', '爽聊视频交友', '很皮语音包',
                     '百合婚恋', '抱抱', '1号玩家', '美篇', '蜜趣', '同城求偶', '附近陌陌约', '珍爱网', '豆瓣', 'Hello语音', '比邻', '聊点', '草莓聊天交友',
                     '月光宝盒直播', '触宝电话', '同城寂寞聊', '世纪佳缘', '吹牛', '玩洽', 'QQ HD mini', '聊天女仆', '葫芦3侠', '附近的人', 'V聊视频聊天',
                     'LOFTER', '分身大师', '闲聊', '开房', '米聊', '95爱播', 'IS语音', '新浪博客', '开心斗', '快猫', '遇到同城交友', '呼呼', '电话手表',
                     'pick语音', '有朋达达', 'TIM', '冒泡', 'Uki', '处CP', '微信多开分身双开助手', '可遇', '百度知道', 'Hi', 'TT语音', '一罐',
                     '微博极速版', '同城约单', '我是谜', '心悦俱乐部', '同城单身约', '有伴', '彩彩', '美团众包', '漂流瓶', '个性头像', '方舟生存进化助手', '第一弹',
                     '他趣', '摸鱼塘', '附近陌陌交友', '和飞信', '积目', '暖暖', '黄瓜视频直播', '旺信', '爱扑'],
            '手机美化': ['装扮少女', '魔秀桌面', '透明手机主题', '壁纸多多', '安卓壁纸', '动态壁纸', '微视频', '字体管家', '小妖精美化', '爱壁纸', '微锁屏', '安卓动态壁纸锁屏',
                     'Cuto 壁纸', '火萤', 'GO桌面', '动态壁纸', '主题美化助手', '小精灵美化', '小妖精美化', '壁纸精灵', 'XP桌面', '字体', '火萤组件',
                     '字体美化大师', '图凌', '小米桌面（主题壁纸锁屏）', '三星主题商店', '指纹密码文字锁屏', '爱字体', 'QQ酷字体', '惠锁屏', '360桌面', '酷炫字体',
                     '桌面萌宠', 'Nova桌面', '搜图神器', '漫芽糖绘画', '微桌面', '一键锁屏', '酷划锁屏', '粉粉女生卡通主题锁屏', '美眉放大镜', '秀壁纸', '小米主题-最主题',
                     '3D宝软桌面', '纹字锁屏', '手迹造字', '一键锁屏', '优美图', '最美壁纸', '曲面闪光', '微软桌面', 'MM大搜索', '锁屏君', '内涵密码锁', 'Hola桌面',
                     'Buzz桌面', '星空视频壁纸', '动漫壁纸锁屏', '华为', '兽耳桌面', '魔幻粒子3D', 'iOS', '壁纸多多', '掀裙查电量：深津京香', '3D山水风景动态壁纸',
                     '动态壁纸大全', '纹字主题', '微主题', 'WANIMAL', '超灵敏指纹解锁', '艺术签名设计专业版', '天天锁屏', '360壁纸', '美人', '好看壁纸',
                     'Tapet随机壁纸', '动态主题桌面', '掌心私房美女', '壁纸神器', 'Win7主题之魔伴桌面主题', '手迹字体', '气泡', '一键锁屏', '换字体管家大师版', '点心桌面',
                     '王者荣耀猎手', '扣扣主题神器', '动漫壁纸', '艺术签名', '桔子壁纸', '91锁屏', '免root更换字体管家', '个性签名设计', '看MM', '屏幕常亮助手',
                     '安卓字体大师', '口袋美人', '王者荣耀圣诞版主题壁纸', 'Next桌面', '方正字酷', '3D人脸识别', '动态壁纸', '触摸美女动态图片', 'OS10桌面', '锁屏大全',
                     '3D壁纸', '奥特曼图片(高清版)', '彩虹堂古装', '美女', '刷钱', '穿透', '艺术签名设计', '锁屏精灵', '全能指纹解锁', '打火机', 'Buzz小部件',
                     '魔幻桌面', '瀑布 的动态壁纸'],
            '新闻阅读': ['趣头条', '一点资讯', '喜马拉雅', '凤凰新闻', '书旗小说', '米读小说', '今日头条', '今日头条', '蜻蜓FM', '追书神器', '搜狗阅读', '快看漫画',
                     '免费小说大全', '全本免费小说阅读器', '韭黄头条', '微博动漫', '起点读书', '全本免费快读小说', 'QQ阅读', '咪咕阅读', '腾讯新闻', '熊猫看书', '微鲤看看',
                     '闪电新闻', '懒人听书', '腾讯动漫', '看漫画', '东方头条', '多多免费书', '热搜小说', '成都发布', '惠头条', '凤凰新闻', '爱上头条', '奇热漫画',
                     '网易新闻', '免费追书', '小马资讯', '天眼查企业查询', '简单阅读', 'Steam', '百度文库', '淘新闻', '触漫', '光明云媒', '漫画岛', '漫画台',
                     '纵横小说', '掌中小说书城', '百度阅读', 'TXT全本免费阅读', '料多多', '漫画人', '天天快报', '新浪财经', '腾讯体育', '听书神器', '七猫免费小说',
                     '17K免费小说', '浙里办', '豆豆免费小说', '金杠杆', 'LoL电竞达人', '一直牛', '动漫之家', '易车', '时刻新闻', '一点资讯', '微信读书', '多看阅读',
                     '想看', '恋爱话术库', '趣追书', 'UC头条', '漫客栈', '搜狐资讯', '社会扶贫', '柠檬免费小说', '即刻', '羞逗', '免费小说', '凤凰资讯',
                     '免费全本小说书城', '腐次元', '宜搜小说', '虎扑', '看理想', '橙光', '布卡漫画', '晋江小说阅读', '知音漫客', '乐玩游戏', '捷报比分', '追书免费全本小说',
                     '有妖气漫画', '酷我听书', '央视新闻', '笔趣阁', '搜狐新闻', '麦小贱', '网易蜗牛读书', '飞卢小说', '咚漫', '快点阅读', '头条快报', 'TXT免费全本小说',
                     '邪恶少女漫画之无翼鸟恋母', '小书亭', '中青看点', 'PDF阅读器 Adobe Reader', '藏书馆', '连尚读书', '免费电子书', '无限漫画', '米赚头条',
                     '免费小说全集', '漫漫漫画', '免费听书', '连尚免费读书'],
            '摄影图像': ['抖音短视频', '微视', '快手', '美图秀秀', 'B612咔叽', 'BeautyCam美颜相机', 'Faceu激萌', '小影', '测谎仪', '全民小视频', '天天P图',
                     '轻颜相机', 'PicsArt美易照片编辑', '无他相机', '美拍', '录屏大师', '快手极速版', '水印相机', '乐秀视频编辑器', 'Biu神器', '微信视频美颜助手',
                     '梦幻修图', '逗拍', 'VSCO Cam手机摄影', 'Photoshop手机版汉化版', '天天看视频', 'VUE Vlog', 'P图大神', 'NOMO 相机',
                     'Snapseed', '头像大师', '稿定设计(天天向商)', 'MIX', '在几个全息图3D开玩笑', '相册管家', '手指触电', '相机360', '美妆相机', '变老',
                     '最美证件照', '简影', '秒拍', 'Wecut', '字说', '快图浏览', '微商水印相', '最美自拍', '黄油相机', '斗图神器', '屏碎 Prank',
                     'LINE FRIENDS', 'Inshot', '图片合成器', 'IMVU Mobile', '画中画相机', '爱看', '快速推特', '玩图', 'GirlsCam',
                     'InShot相机', '时光相册', '马卡龙玩图', 'Facetune', 'Adobe Photoshop Express', 'V380', 'Snapseed照片编辑', '彩视',
                     '蒸汽波相机', '格式工厂', 'PicsArt美易绘画', '3D全息图 Simulated', '360智能摄像机', '图片加文字秀', '迷你魔幻粒子世界', '云美摄视频创作',
                     '大片', '聊天机器人', 'Autodesk Pixlr', 'Sphoto', 'in', '指纹解锁', '蛇在屏幕上恶作剧', '鬼影相机(Horror Camera)',
                     '图片加文字', 'MediBang Paint', '搞怪照片', '照片编辑器', 'Instadown', '拼图酱', '神段子', '分数导师', '装酷神器', '美人相机',
                     '元道经纬相机', '趣推', '天天向商', 'Macaron Pink', '魔漫相机', '整人屏幕', '简拼', '动感相册', 'Foodie', '图片搜搜', 'POCO相机',
                     '图库', '装逼神器', '屏幕录像', '快去水印', 'Layout 组合照片', '玩图美妆', '超级录屏', '录屏专家', '绅士领域', '智能证件照', 'MYOTee脸萌',
                     'TouchRetouch 抠图大师', '全能相机', '小蚁摄像机', '图片编辑工具', 'Uber优步'],
            '考试学习': ['作业帮', '掌门1对1辅导', '驾考大师', 'myOffer', '快对作业', '安全教育平台', '作业互助组', '小猿搜题', '车轮驾考通', '驾考宝典',
                     '作业盒子小学学生端', '一起小学学生', '准题库', '托福考满分', '英语流利说', '教师资格证随身学', '教师资格证帮', '考满分词汇', '初级会计职称随身学',
                     '基金从业资格考试题库随身学', '会计对题库', '会计职称对题库', '作业帮家长版', '普通话学习测试', '洋葱数学', '中大网校', '会计考试准题库', '公务员准题库',
                     '网易有道词典', '日本村日语', '初级会计职称准题库', '考研准题库', '有道翻译官', '英汉字典', '雅思考满分', '对啊基金从业对题库', '百度翻译', '学习通',
                     '百词斩', '教师资格证对题库', '作业精灵', '晓黑板', '对啊CMA考试随身学', '驾校一点通', '学霸君', '公务员', 'Google 翻译', '古筝',
                     '侠盗街头犯罪模拟', '口语100', 'GRE3000词', '作业答案', 'GMAT考满分', 'GRE考满分', '会计随身学', '有道口语', '证券从业随身学',
                     '银行从业随身学', '人力资源经济师随身学', '注册会计师随身学', '证券从业资格对题库', '不做手机控', '乐教乐学', '智学网', '小猿口算', '金融考试帮',
                     '一起中学-学生', '网易公开课', '火柴蜘蛛侠英雄2', '阿凡题', '记忆力训练', '驾考家园', '英语趣配音', '检查作业', '超级玛丽', '不背单词', '3D模拟驾驶',
                     '执业药师准题库', '知到', '金山词霸练口语', '有道精品课', '中国大学MOOC', '爱作业', '家长盒子', '猿题库', '考拉阅读', '火柴蜘蛛侠英雄', '恐龙快打',
                     '好分数学生版', '作业盒子小学老师端', '英语电台', '学而思网校', '扇贝单词', '好大夫医考', '翻译君', '驾考宝典科目一', '英语翻译', '掌门1对1辅导',
                     '天天练', '微课掌上通', '作业通', '班级优化大师', '三国志官方版', '星火英语', '可可英语', '汉语字典', '作文纸条', '眠眠学法', '出国翻译官',
                     '小学英语伴读人教版', '小学语文数学英语同步', '驾考一点通', '新华字典', '充电了么', '我要自学网', '天天中彩诗', '宝宝数多少', '街头霸王2', '微入学院',
                     '升学e网通', '扇贝听力', '小学作业答案'],
            '网上购物': ['淘宝', '当当', '拼多多', '丝芙兰SEPHORA', '京东', '美团', '小红书', '云淘集', '苏宁易购', '转转', '小黑鱼', '唯品会',
                     '阿里巴巴1688批发', '闪送', '斗牛(原蜂潮)', '大众点评', '返利淘联盟', '光汇云油', '乐分期', '玉龙云集', '闪油侠', '十色成人两性情趣', '菜鸟裹裹',
                     '得意淘', '安逸淘优惠券', '淘集集', '返利优惠券联盟', '网购联盟', '购物返利联盟', '省钱优选联盟', '返利省钱联盟', '网易考拉', '贝店妈妈的轻创业平台',
                     '一淘', '快递100', '77分期', '红豆角', '省钱快报', '花生日记', '二手手机找靓机', '交易猫', '一亩田', '淘宝特价版', '一起买买买', '京东到家',
                     '返利', '小牛微投资天天赚钱软件', '黄金象', '惠农网', '友米乐 - 越卖越便宜', '淘聚聚', '盒马', '蘑菇街', '小米商城', '分期乐', '顺丰速运', '优惠加',
                     '千牛', '手游赚', '网易严选', '趣到账', '亚马逊购物', '华为商城', '淘宝联盟', '微店', '识货', 'e城e品', '王者皮肤盒子', '零用钱', '招联金融',
                     '云集微店', '优惠券', '熊猫优选', '饿了么星选', '小米有品', '什么值得买', '淘券多多', '淘宝HD', '堆糖', '微店店长版', '聚美', '国美',
                     '夜欲两性情趣商城', '每日优鲜', '应有', '康宝莱订购', '微快递', '美团骑手', '折800', '苏宁小店', '格调乐家', '贝贝', '小象优品', '百度糯米',
                     '蜜源', '零售云', '蜜芽宝贝', '美色成人情趣内衣', '淘粉吧', '咸鱼网', '爱回收', '印变有品', '聚划算', '网易藏宝阁', '绿叶商城', '快手刷粉丝',
                     '婚礼纪', '购省钱', '货车帮货主', '每日一淘', '淘手游', '酒链世界', '康爱多掌上药店', '梦幻藏宝阁', '每日好价省钱优惠券', '爱上街', '一折特卖',
                     '环球捕手', '券妈妈优惠券'],
            '金融理财': ['支付宝', '恒信贵金属', '融360', '团贷网', '云闪付', '信用星球', '还呗', '薄荷好借', '速借贷', '分期还', '中国建设银行', '借钱花呗',
                     '农行掌上银行', '工行手机银行', '翼支付', '中国银行', '邮储银行', '宜人贷借款', '京东金融', '拿下钱包', '360借条', '平安金管家',
                     '人人淘金现货微赚八元投资', '信用飞', '新浪会选股', '国金普惠', '搜易贷', '招商银行', '买单吧', '工银融e联', '手机贷', '拍拍贷借款', '易港金融投资理财',
                     '钠镁股票', '平安普惠', '用钱宝', '团贷网', '向钱贷', '平安口袋银行', '51信用卡管家', '足球胜负彩', '信而富投资', '点掌财经', '和包支付',
                     '人人贷借款', '银谷在线', '交通银行', '极速借钱贷款借款', 'MetaTrader4外汇交易平台', '钱桌子理财', '股掌柜', '浦发手机银行', '趣花分期',
                     '同花顺炒股票', '小米贷款', '有料股票炒股配资', '立即贷', '500彩票', '弘历Chart', '360贷款导航', '凤凰金融', '网上赚钱-兼职理财投资神器', '来分期',
                     '广发证券易淘金', '助力钱包', '平安健康', '北京赛车pk10', '闪银', '贷上钱', '随手记', '借点钱贷款', '十元淘金商城交易软件', '快贷',
                     '云商城微理财交易平台', '掌上掘金商品交易软件', '聚料', '智慧财', '大象期货', '快涨股票', '期货', '大公鸡七星彩', 'e宝账', '陆金所', '2345贷款王借款',
                     '高财生金服理财', '去哪借', '中国体育彩票', '广发手机银行', 'i云保', '捷信金融', '萌橙理财', '你我贷借款', '借花花贷款', '贷款助手', '重庆时时彩',
                     '微贷钱包', '创客金融理财投资', '十元易购', '中信银行手机银行', '动卡空间', '发现精彩', '大智慧', '有钱花（原百度金融信贷）', '信用管家借钱', '省呗',
                     '一元赚', '安逸花', '借呀', '外汇投资', '小赢卡贷', '正合钱包', '现金借款', '中银国际', '天天中彩票', '兴业银行', '重庆时时彩分析软件', '光大银行',
                     '时时彩', '花钱无忧', '蛋花花', '我来贷'],
            '生活休闲': ['每日头像', '51米多多', '货拉拉', '土巴兔装修', '安居客', '58同城', '饿了么', '10086', '闲鱼', '海尔洗衣', '口碑', '交管12123',
                     '中国移动', '美团外卖', '墨迹天气', '联通手机营业厅(官方版)', '社保掌上通', '车轮', '汽车报价大全', '2345天气王', '电信营业厅', '汽车之家',
                     '多开分身', '广东移动手机营业厅', '油莫愁', '瓜子二手车', '快牙', '车行易查违章', '万年历', '懂车帝', '前程无忧51Job', '三个阿姨', '赚钱宝',
                     '兼职咸鱼-学生赚钱', '微信定位精灵', '纽扣助手', '指趣助手', '早游戏', '贝壳找房', '智联招聘', '加一次元', '赶集网', '手机监控', '遥控精灵',
                     '途虎养车', '平安好车主', '天猫精灵', '种子搜索', '网赚', '掌上兼职', '文字转语音', '今日招聘', '中华万年历', '下厨房', '荒岛求生:进化', '叉叉云游',
                     '空调万能遥控器', '天气预报', 'Boss直聘', '谷歌搜索', '果盘游戏', '手机照片恢复', '房天下', '手电筒', '乐播投屏', '空调遥控器', '掌上电力',
                     '点点花', '肯德基', '红包捕手', '多功能助手', '链家', '微工程', '天气通', '望远镜', '手机号码定位跟踪', '超信', '格来云游戏', '掌上道聚城',
                     '电竞资讯', '格力员工商城', '万能遥控器', '小睡眠', '小米遥控器', '疾风bt种子下载', '手机万能变声器', 'CCB建融公寓', '那好吧', '皮皮搞笑', '邪恶漫画',
                     '物流帮手', '天下游', '通讯录短信群发平台', '手机彩票', '12123', '计算器', '心意红包', '加油广东', '浙江移动手机营业厅', '温度计', '皮皮蟹语音包',
                     '233小游戏', '悟空遥控器', '全国违章查询', '泰拉瑞亚盒子', '虚拟定位王', '四川移动掌上营业厅', '56智能卡管家', '社保一点通', '室内温度计',
                     '江苏移动掌上营业厅', '多多计算器', '球探体育比分', '全国违章查询', '人人车二手车', '安徽移动手机营业厅', '空调手机遥控器', '我查查', '葫芦大侠',
                     'Boss直聘高薪版', '掌上看家采集端'],
            '旅游出行': ['高德地图', '同程旅游', '携程旅行', 'Booking.com', '嘀嗒出行', '去哪儿旅行', '12306官方版', '滴滴出行', '小马跨境车', '腾讯地图',
                     '滴滴车主', '朋友手机定位', '飞猪', '首汽约车', '北斗地图', '车轮转车服', '马蜂窝旅游', '谷歌地图', 'ofo小黄车', '北斗导航', '奥维互动地图',
                     '贵阳地铁-官方APP', '车来了', '掌上出行', '货拉拉司机版', '摩拜单车', '蚂蚁短租', 'Google地球', '高德地图HD', '途牛旅游', '智行火车票',
                     '同程旅游', '途家民宿', '高铁管家12306火车票抢票', '顺风车', '航旅纵横', '天眼', '12306买火车票', '华住酒店', '嘀嗒出租司机', '曹操专车',
                     '易通行', '百度地图位置监护', '神州租车', '卫星地图', '墨迹天气极速版', '首约司机', '百度CarLife', '春秋航空', '南方航空', '广州地铁', '飞常准',
                     '无忧行', '顺风车司机端', '布丁生活', '嘀哒司机', '六只脚户外线路', '路路通', '凯立德导航', '超级指南针', '高德导航-intel定制版', '全能出行',
                     '公交到哪了', '顺风车', '滴滴顺风车', 'GPS 卫星地图导航', '艺龙旅行', 'Gofun出行', '上海移动和你', '神州专车', '虚拟定位', 'GPS工具箱',
                     'Booking.com', 'e路合乘', '酷米客', '亿连驾驶助手', '中国国航', '智能公交', 'GPS导航', '一嗨租车', '铁友火车票', '美团打车司机', '航班管家',
                     '手机全球定位监控', '联动云租车', '乐养云', '皇包车旅行', '坐公交', '差旅天下', '8684公交', '中国地图', '搜狗地图', '美团打车', '携车网', '车到哪',
                     '易到车主端', 'e代驾', '掌上公交', '两步路（户外助手）', '安全守护2', '小猪短租', '地球', '巴士管家', '身份验证器', '手机号码定位', '首旅如家',
                     'EVCARD', '公交e出行', '交运通', '手机公交', 'GPS手机定位', 'WarmCar', '12306掌上火车票', '盛名时刻表', '旅游年票一卡通yong',
                     'e代驾司机端', '快的打车', '东莞通', '租租车', 'GPS手机导航', '菱菱邦'],
            '健康运动': ['平安好医生', '水滴筹', 'Keep', '妙健康', '怀孕管家', 'L8STAR', '毒', '护眼宝防蓝光', '指纹血压', '妈妈网孕育', '小米运动', '美柚',
                     '壹点灵心理咨询', '孕迹暖暖', '华为运动健康', '公共卫生服务平台', '体检宝测血压视力心率', '潮汐', '优健康', '咕咚', '哈啰出行', '计步器', '蜗牛睡眠',
                     '悦动圈', '好大夫在线', '北京一卡通', '壹心理', '乐动力', '小肚皮', '莱聚+', '羞羞', '薄荷健康', '伊美信微整形', '华为穿戴', '微医', '大姨妈',
                     '血压测量', 'OKOK', '艺术正流行', '花百科', '你今天真好看', '血压检测仪', '每天十个妞', '3Dbody解剖', '1药网', '天天血压', '悦跑圈',
                     '幸运106', '电力设备电线电缆平台', '禁毒在线', '懒人护眼', '趣步行', '春雨计步器', '微计步', '乐心运动', '每日瑜伽', '健客网上药店', '快速问医生',
                     '我的社保', '名医汇', '女生日历', '华医通', '云朵护眼', '预约挂号网', '爱康约体检查报告', '重庆社保', '药店药房网商城', '乐动健康', '康康在线',
                     '血压监测器', '魔术教学', '月经期安全期助理', '夜间助手', '北斗地图', '东方韵', '广场舞多多', '阿虎医考', '经络穴位图解', '健身助手', '魔方学院',
                     '口腔执业医师考试阿虎题库', '华斯达克', '步道乐跑', 'MiniOrange', '动动', '中药大全', '北京协和医院', '时间记录器aTimeLogger', '春雨医生',
                     '临床指南', '食物库', '天天护眼', '女生记账', '自学武术', '护目镜增强版（屏幕调节器）', '种子习惯', '安全期日历', '用药助手', '大姨妈神器',
                     '花生备孕月经排卵怀孕管家', 'Now正念冥想', '水滴筹', '眼萌', '瘦瘦', '多锐运动', '拍照识花', '每日养生', '柚宝宝', '运动世界校园', '中医偏方秘方',
                     '新氧美容', '纯诱', '即刻运动', '好体知', '咪咕善跑', '涨姿势V1.0', '完美囚徒健身', '米兔手表', '微脉', '手环', '快证通证件识别'],
            '办公商务': ['百度网盘', '运满满司机', '微信分身版', '招才猫直聘', '猎聘', 'WPS Office', '钉钉', '个人所得税', 'QQ邮箱', '扫描全能王', '保险师',
                     '微信分身版免费', '群发助手', '微商', '排班日历', '香蕉记', '手机克隆', '黄历', '云电脑', 'CAD快速看图', '微云', '江苏工商', 'CAD看图王',
                     '网易邮箱', '企业微信', '微信群发', '信贷360', 'Microsoft Word', '微信加粉', '手机电脑', '微信群发', '微信清粉', '139邮箱',
                     '网易邮箱大师', 'TeamViewer远端控制版本', '115', 'Microsoft Excel', '江苏企业年报', '平安口袋e行销', '隆基HRSSC', '小麦助教',
                     '印象笔记', '番茄ToDo', '百度云网盘三星定制版', 'Daniu大牛', '有道云笔记', '企查查企业信用查询', '启信宝', '运满满司机', '天眼查', '微商工具箱',
                     'WPSOffice纯净版', '备忘录', '白描', '微信分身版', 'Gmail', '饿了么商家版', '滴答清单', '思维导图', '今日招标网-政府招投标采购平台', '小日常',
                     '实名宝', '非煮不可', '多开虚拟精灵', '记事本', '云助理', '多益云', '录音宝', 'Microsoft PowerPoint', 'PIXMA Print', '讯飞语记',
                     '360安全云盘', '锤子便签', '新浪微盘', '微商相册', '时间表', '微信分身', '闽政通', '微信多开', 'word办公文档', '睡眠小镇', 'OneNote移动版',
                     '乐同步', '奇妙清单-任务管理', '福昕PDF', '手机Word', '189邮箱', '云之家', 'CAD手机看图', 'TeamViewer QuickSupport',
                     'WPS便签', '幕布', 'Office Mobile', '日历', '易企秀', '天翼云盘', '找到', '个性艺术签名-精品', '菜鸟包裹侠', '计算管家', '作家助手',
                     'Zoom', '太易云电脑', 'Hi-Q MP3录音机', '平安商户管家', 'Microsoft\xa0Outlook', 'Outlook邮箱', '晒书房', '汇通销售宝',
                     '石墨文档', '文字扫描王', '水滴清单', '刷赞神器', 'OneDrive', '建工计算器', '墨记-日记和笔记', '名片全能王', 'CAD迷你看图', 'Cortana',
                     '移动协同', '移动办公'],
            '育儿亲子': ['兔耳故事', '妈妈帮', '凯叔讲故事', '贝乐虎儿歌', '宝宝行为认知', '宝宝巴士奇妙屋儿童早教', '樱桃小利', '小伴龙', '宝宝超市', '纳米盒', '奇妙料理餐厅',
                     '电e连', '宝宝时尚设计师', '儿歌多多', '奇妙怪物医院', '宝宝梦想小镇', '猫小帅学汉字', '村长讲故事', '宝宝手工零食', '宝宝巴士游乐园', '化妆小公主',
                     '宝宝医院', '宝宝巴士', '掌通家园', '宝宝树孕育', '宝宝巴士乐园', '雪糕工厂', '宝宝小当家', '奇妙咖啡餐厅', '宝宝甜品店', '宝宝冰淇淋工厂', '叽里呱啦',
                     '奇妙蛋糕店', '宝宝汽车城市', '宝宝假日旅行', '儿歌点点', '宝宝知道', '小企鹅乐园', '奇妙逻辑冒险', '公主涂色秀', '孩子画画', '家长通', '小魔女传奇',
                     '宝宝调色屋', '宝宝神奇汽车', '爱奇艺奇巴布', '宝宝星际厨房', '宝宝从哪来', '宝宝森林美食', '我的乐高城市世界2', '宝宝日常安全', '宝宝动物世界', '宝宝幼儿园',
                     '快乐小鸡爱生蛋', '宝宝迷宫大作战', '宝宝学数字', '照顾小宝宝', '宝宝当店长', '中国式家长', '宝宝巴士儿歌', '宝宝居家安全', '奥特曼终极大战', '乐高我的城市',
                     '闪到', '宝宝果汁商店', '小公主成长记 - 免费儿童游戏', '宝宝认工程车', '宝宝来了', '宝宝学汉字', '四季知多少', '妈咪宝宝树', '多少個孩子',
                     '看你错吃了多少废物', '多少钱', '恐龙王国', '亲宝宝', '糖果工厂', '宝宝飞机场', '童鸽AR地球仪', '钢琴教练', '时尚衣帽间', '物理画线', '宝宝地震安全',
                     '化妆模拟器', '麦田拼音', '宝宝恐龙家园', '宝宝爱整理', '奇妙春游日', '迷你乐高世界', '宝宝梦想职业', '宝宝爱吃饭', '悟空识字', '智慧树', '宝宝开车大冒险',
                     '贝瓦儿歌', '跟我学写汉字', '宝宝学颜色', '宝宝水果沙拉', '宝宝运动会', '宝宝出行安全', '宝宝小船长', '宝宝小牙医', '我是消防员', '学画画 (先进)',
                     '宝宝地震安全3', '男人最爱玩游戏', '宝宝地震安全2', '自己上厕所', '小豆苗疫苗助手', '小猪佩奇十万个为什么', '公主的梦幻舞会', '宝宝睡前故事大全', '宝宝隐私安全',
                     '精灵公主魔法换装', '家长帮', '双胞胎成长记', '时尚明星之换装达人', '宝宝爱水果蔬菜', '欧布奥特曼', '宝宝认蚂蚁'],
            '休闲益智': ['PUBG MOBILE（绝地求生：刺激战场 国际服）', '贪吃蛇大作战', '球球大作战', '我的世界夏季版', '拉斯维加斯犯罪模拟', '黑洞大作战', '开心消消乐',
                     '奥特曼格斗进化1', '节奏大师', '小鳄鱼爱洗澡', '火柴人越狱6', '单挑荒野', '当妈模拟器', '天天爱消除', '像素人吃鸡', '疯狂木偶人', '血腥射手',
                     '海绵宝宝海底冒险', '滚动的天空', '红蓝大作战2', '蜘蛛侠之保卫城市', 'QQ炫舞手游', '弗洛伦斯', '孤岛求生', '火柴人绳索英雄迈阿密', '撞头赛车',
                     '消灭星星全新版', '鲍迪斯的恐怖奶奶', '钢琴块2', '装扮女孩', '猎车匪帮', '极品飞车：最高通缉', '世界大战：最后的堡垒', '芭比梦幻屋冒险', '女生迷你世界',
                     '老爸曾是小偷', '创造与挑战', '机器人绳索英雄', '美国突击队：战场幸存者', '蜘蛛机器人', '饥饿鲨：进化', '鳄鱼小顽皮爱洗澡（LITE版）', '我的安吉拉',
                     '探索迷你世界', '侏罗纪孤岛求生：方舟2', '脑点子', '维加斯黑帮', '波克捕鱼', '青蛙模拟器', '一起玩捕鱼', '欧洲卡车司机', '攀爬侠', '逃跑吧！少年',
                     '还有这种操作2', '超级兔子人', '跳舞的线', '刺激战场', '超级玛丽', '疯狂像素人', '超级粘液模拟器2', '黑帮小丑', '火柴人绳索英雄犯罪', '火柴人犯罪',
                     '像素绝地求生', '狗狗巡逻队：营救任务', '中华美食-宝宝巴士', '警察追捕行动', '洛杉矶犯罪', '拆散情侣大作战2', '采油小怪2：生日派对', '蜘蛛侠城市枪击战',
                     'Evertech Sandbox', '我的汤姆猫', '捕鱼大作战', '守护你前行', '我的世界冬季版', 'PopStar消灭星星', '纪念碑谷2', '越狱 完美版',
                     '水果忍者终极版', '小猪佩奇:运动会', '交警模拟器', '迷你像素射击沙盒世界', '欧洲卡车司机2018', '迷你的世界', '像素车', '犯罪冲突:疯狂的圣安地列斯',
                     '越野巡洋舰模拟器', '冰箱里的布丁被吃掉了', '口袋妖怪：漆黑来临', '海滨消消乐', '火柴人绳索英雄3：警察射击', '皇家战场吃鸡战', '布林机', '军队战争模拟器',
                     '战争模拟器2', '山羊模拟器', '荒野丛林生存', '俄罗斯方块', '绳索英雄', '奇妙农场——宝宝巴士', '瘟疫公司', '开心躲猫猫', '弓箭手大作战'],
            '跑酷竞速': ['QQ飞车', '地铁跑酷', '神庙逃亡2', '城市汽车驾驶模拟器', '大卡车模拟器', '出租车接客2', '天天酷跑', '驾驶学校2017', '越野汽车驾驶模拟器3D：爬坡赛车',
                     'Drive To City', '汤姆猫跑酷', '真实赛车3', '越野卡车模拟运输', '飞机真正的飞行模拟器', '越野驾驶：沙漠', 'Heavy Bus Simulator',
                     '世界卡车驾驶模拟器', '蜘蛛侠之城市英雄', '极品飞车：最高通缉', '神偷奶爸：小黄人快跑', 'Drive Ahead!',
                     'Grand Crime Mega City: Gangster City Crime Theft', '登山赛车', '憨豆先生：环游世界', 'The Frog Amazing 3D 2',
                     '出租车接客', '真实停车模拟器2018', '真实汽车模拟驾驶', 'My Real Car Nitro 2019', '驾驶学校2016', '喵星大作战',
                     'Ultimate Car Driving Simulator', '疯狂动物城：赛车嘉年华', 'Supermarket Gangster Escape 3D', '大型越野车模拟',
                     'Go To Street', '越野美国陆军运输辛', '高校模拟器2017', '公交模拟', '登山赛车之天朝历险', '火柴人毁灭4：湮灭', '极限摩托 精简版',
                     'Extreme Off-Road Racing', 'Gangster Crime Car Simulator',
                     'Real Snowy Police Car Simulator 2019 3D', 'Car Accident 2018 - Crash Cars',
                     'ES Bus Simulator ID 2017', 'Crime Santa Claus Rope Hero Vice Simulator',
                     '在 卡车 驾驶 游戏 ： 高速公路 道路 和 曲目', '极限着陆', '卡车模拟器2018', '越野车爬上：泥泞驾驶', '奔驰S600漂移模拟器',
                     'Happy Bicycle Wheels', '长途大巴模拟器', '精英军训练免费', 'Offroad Truck Simulator 2018', '登山赛车2', '一起来飞车',
                     '挖掘机机器人', '不可能的BMX自行车特技', 'PUBG Weapon Sounds', '模拟建造2', '不可思议的自行车', '飞行机器人城市救援',
                     'Car Parking Bmw i8 Simulator', '天天飞车', '水滑下坡', '美国警察机器人狗-警察飞机运输游戏', 'World Crash Car',
                     'Superheroes Bus Stunts Racing', '水 公园 游戏： 特技 人 跑', '真实赛车2', '愤怒的老奶奶玩跑酷', '地铁公主赛跑者',
                     'Guides Gangstar Vegas 5 Game', 'Off-Road Cargo Truck Driver: Climb Hill Simulator',
                     '大欧洲卡车停车传奇 Grand Euro Truck 3D', 'Car Parking Audi A6 Simulator', '油油船运输车卡车模拟器',
                     'Aventador Drift Simulator', 'Real Car Driving Simulation 18', '超车小能手', 'X5 M40 and A5 Simulator',
                     'Super Hero Bike Mega Ramp Impossible Stunts Racing', '卷烟模拟器',
                     'Beach House Builder Construction Games 2018', '越野凯雷德4x4驾驶', 'City Road Excavator Simulator 2018',
                     '欧洲卡车模拟2', 'MTB下坡：多人', '重型挖掘机起重机：建设城市卡车3D', 'Euro Truck Simulator 2017', '极限汽车驾驶模拟器2', '熊大跑酷',
                     'Euro City Trucks Driving 2017', 'Go To Town 2', '蜘蛛侠跑酷', '宇通巴士模拟',
                     'Crane Simulator : Construction Pro City Builder 3D', 'Endless Run : Magic Temple', '疯狂的兔子狂奔',
                     '激流快艇3', 'Tom Clancy’s : battle Ghost Recon', 'Serçe Racer', '汽车人大破坏2', '熊出没2',
                     'Euro Driving Truck Simulator', '至尊长途汽车模拟器3D', '越野泥亚军卡车模拟3D：旋转轮胎 MudRunner Truck Simulator',
                     '卡车模拟器：欧洲2', '巴士酷跑'],
            '扑克棋牌': ['欢乐斗地主', 'JJ斗地主', '欢乐麻将', '天天象棋', '中国象棋', '英雄杀(官方版)', '中国象棋单机', '单机斗地主（开心版）', '五子棋', '欢乐麻将最新版',
                     '麻将来了', '闲来广东麻将', '单机斗地主Q版', '真人斗地主2', '经典中国象棋', '积分斗地主', '单机麻将大全', '单机斗地主-单机离线全民欢乐天天斗地主棋牌游戏',
                     '斗地主来吧', '五子棋', '中国象棋', '欢乐真人麻将', '单机版斗地主HD', '随便跑得快', '拖拉机 升级', '四川麻将', '欢乐逗地主', '象棋大师.中国象棋',
                     '围棋', 'JJ经典麻将', '单机斗地主（六月）', '单机象棋游戏', '单机斗地主－无流量', '快乐飞行棋', 'Excel三国杀', '快乐麻将', '军旗', '斗兽棋',
                     '跑胡子（字牌）合集', '途游斗地主', 'QQ欢乐升级', '贵阳麻将之捉鸡', '中国象棋', '天天斗地主', '中国象棋高智能单机版', '麻将单机版', '天天斗地主（真人版）3',
                     '升级', '麻将免费', '国际象棋', '中国跳棋', '欢乐中国麻将', '蜘蛛紙牌', '够级', '真人天天斗地主', '欢乐围棋', '乐享四人斗地主', '弈城围棋', '皇冠斗牛',
                     '泸州大贰', '街机水浒传OL', '中国象棋', '欢喜斗地主', '同城游打大A', '象棋巫师', '军棋', '游戏王(汉化版)', '中国象棋棋谱', '同城游四川麻将',
                     '绝美斗地主', '军棋决战', '蜘蛛纸牌', '大头斗兽棋', '坦克风暴战争', '湖南快乐打筒子扑克', '飞行棋大战', '中国象棋经典版', '保皇', '蜘蛛纸牌(经典版)',
                     '军棋对战', '途游中国象棋', '真人麻将', '老友内蒙麻将', '五子棋[单机双人对战版]', '我爱斗地主', '动物街机汇', '明星三缺一国标版2014', '乐清麻将武汉花',
                     '单机游戏中心', '游戏王YGOMobile', '美女视频斗地主', '十三道'],
            '动作冒险': ['拥挤城市（Crowd City）', '奥特曼格斗进化0', 'Granny', '木筏求生：绝地生存', '荒岛生存', '贪婪洞窟2', '火柴人战争遗产', '拳皇97',
                     '火柴人侠盗飞车3D', '狗狗巡逻队跑酷', '火力全开2：城市狂热', '枪和狙击手', '绳索英雄4', '迷你像素世界', 'Adventure Spiderman Run', '机器鲨',
                     '恐怖修女', '植物VS僵尸', '黑洞大吞噬', '边境之旅', '绳索英雄蜘蛛侠', '特种部队小组2', '我的矿工世界', '我的世界之求生岛', '钢铁侠：城市保卫', '山岭巨人',
                     'New Fornite Battle Royale Hint', '刺客信条：血统', '忍者必须死3', '荒岛求生', '被尘封的故事', '海洋木筏求生',
                     'Superhero Frog Amazing Adventure', '拳皇命运', '陨石60秒!', '侏罗纪世界：竞技', 'Raft Craft', '生存森林工艺', '恐怖之眼',
                     '奥特曼传奇英雄', 'Spider Hero Miami City Fight', '陆军突击队生存任务', '流行战争', '大猩猩变形金刚大战', '超级英雄怪物大城战役',
                     '纸片大作战2', '生存岛：创造模式', '不思议迷宫', '危鸡之夜', '木筏生存岛逃生', '警察机器人马游戏', 'Forces of Freedom (Early Access)',
                     '变形金刚：飞行鲨', '激斗英雄奥特曼', '火柴人联盟2017修改版', '摧毁房子', '海上木筏生存', '乐高：我的城市2', '超级蜘蛛奇怪的战争英雄', '高校模拟器2019',
                     '泰拉瑞亚', '生物迷宫战争', '口袋妖怪:红宝石', '3D邪恶蜘蛛人', '我的海盗船世界', '饲料鱼和成长', '口袋妖怪：釉色', '司机先生', '空岛生存', '吸血鬼变身领主',
                     '街机厅', '火柴人对打', 'Oceanborn: Raft Survival Craft', 'Fire boy in the Golden Ice Temple', '愤怒的火柴人5',
                     'Fit', '精灵宝可梦-外传', '末日方舟', '英雄大作战', 'Master Craft', '蜘蛛侠超级英雄', '口袋妖怪 火红', '采油小怪', '弄死火柴人2',
                     '拳皇2000', 'Mine and Craft - Lonely Island', 'Guide BIMA-X Satria Heroes', 'Shark vs Raft',
                     '模拟山羊破坏世界', '口袋妖怪：梦的光点', '荒岛求生3D', 'ARK Survival Island Escape', '筏逃生故事筏生存', '3D自由城：卧底 FreeRoam3D',
                     '无人岛生存', 'West Gunfighter', '激斗英雄奥特曼', '僵尸战争：部落冲突', '突变蜘蛛英雄', '合金弹头',
                     'Perfect Pixelmon world for craft &amp; build : 3D PE', 'Frog Super Amazing Simulator', '车祸英雄',
                     '恐龙快打', 'The Grand Rampage: Vice City'],
            '飞行射击': ['绝地求生：刺激战场', '香肠派对', '绝地求生：刺激战场体验服', '堡垒之夜', '绝地求生全军出击', '荒野行动', '王牌战争', '德军大逃杀', '乱斗火柴人', '元气骑士',
                     '魂斗罗：归来', '终结者2：审判日', '生死狙击', '突击队行动：吃鸡战', '生存战争吃鸡战', '弓箭手大作战', '突击队幸存者',
                     'Counter Terrorist Sniper Shoot', '王国纪元', '小米枪战', '虚拟世界', '激斗火柴人', '像素绝地吃鸡', '反恐袭击',
                     '代号47：狙击（测试服）', '飞机模拟', 'Counter Terrorist Frontline Mission: FPS V2', '战地生存', '战场工艺生存', '英雄枪战',
                     '荒野大作战', '警察鹰变形金刚大战', '射击战争', '城市狙击手3D', '火柴人战斗模拟器', '别动队 最终 射击 任务 2018', '史诗战斗模拟器2', '枪神对决',
                     'Infinity battlefield Ops: Free Shooting Games FPS', '警察机器人英雄', '全民枪战2',
                     'Stickman Hero Mafia Vegas Crime', '小小突击队', '像素荒野大逃杀', '坦克世界闪击战', 'Rawenfield',
                     '军队 计数器 恐怖分子 攻击 狙击兵', 'Witherbuster Mod for MCPE Addon', 'Stickman Counter Terror Strike', '闪电突击队',
                     '我的世界之恐龙猎人', 'Weaphones: Gun Si...', '射击风暴', '坦克连', 'Call Of Sniper BattleField Shooter',
                     'Beast Animal Kingdom Battle Simulator: Epic Battle', '突击队丛林作战2040', '弹弹堂', 'F18舰载机模拟起降',
                     '迪亚士：哥哥的勇气', 'World War 2 Battleground Survival Winter Shooter', '狙击手训练街', '终极蜘蛛英雄冒险',
                     'Crowenfield', 'Call Of Duty WW II', '精英狙击手突击队射手：战争英雄生存', 'Battle Simulation', '超级战车大作战',
                     '直升机 机器人 游戏 - 机器人 转变 2018', 'Naxeex Superhero', '战舰世界闪击战', '正义枪战', '极限Stickman模拟器 - 战争游戏',
                     '荒野行动狙击训练场', '火柴人绳索英雄3', '模拟空战', '直升机空袭完美版', '救援机器人改造救火车模拟器', '极限着陆直装版', '现代战机', '维克斯堡之役',
                     '像素绝地吃鸡', '冒险岛Ⅲ', '火线精英', '僵尸世界：生存', '反斗联盟', '环太平洋怪兽之战', 'FPS 游戏： 现代狙击手', '俄罗斯潜艇机器人变形战斗模拟器',
                     '武装直升机', 'Army Men Toy War Shooter', '模拟二战枪支', '喷射派对', 'N.O.V.A.传承战记', '模拟器 火柴人：战士之战', '单机CF',
                     '汽车大逃杀', '90坦克大战(经典版)', '百年战争', '难以置信 怪物 市 英雄', '枪械爱好者', '现代狙击射击', '猎鹿人2014完美版',
                     'Stick Fight Rope Hero 3 Vice Town: Police Shooter', '武器模拟器', '飞行模拟：3D客机', '王者军团',
                     '反恐特警 - Counter Terrorist', 'Weaphones™ Gun Sim Free Vol 2', '集结号捕鱼', '第二次世界大战：精英战场生存'],
            '经营策略': ['梦间集', '僵尸榨汁机', '攻城掠地', '保卫萝卜3', '列王的纷争', '迷你世界', '王者荣耀体验服', '欧洲卡车模拟', '拆散情侣大作战.', '心动女友',
                     '植物大战僵尸2', '快乐玻璃杯', '高校模拟器2018', '植物大战僵尸2', '奶块', '少女都市3D',
                     'New Human Fall Flat Guide Walkthrough', '学校女生模拟器', '我进不去学校了', '我的游戏世界', '找到老公的私房钱', '植物大战僵尸：英雄',
                     '奇迹暖暖', 'The Human Fall : Flat Hints', '妈妈把我的游戏藏起来了3', 'Pixelmon mod for MCPE (Addon)', '建桥专家!',
                     '找到老婆的私房钱', 'Guide Amazing Frog New 2018', '木水火土', 'Guide Scrap Mechanic Game', '王国保卫战：复仇',
                     'Granny Santa Claus (No Ads)', 'Guide Ravenfield Game 2018', '最后她对我说', 'Ravenfield Hints New 2018',
                     '粘液模拟器2018', '我的世界-女孩版', '模拟城市：我是市长', 'New Аvenger add-on for MCPE', 'Human Fall Flat Tips',
                     'MOD Coordinates Unlocker', '辐射避难所', '小猪佩奇：主题乐园', '终极史诗战役', '逃课大作战', 'Super Car F. Mod for MCPE',
                     '真正的X射线模拟器', '亲吻小游戏', 'Tricks:Plants vs. Zombies 2', 'Tips for Scrap of Mechanic', '掌上激光笔笑话',
                     '证明：她是我女友', '校园时装店', '开心火锅店', '保卫萝卜2', '托卡生活：邻居', '保卫萝卜(官方中文版)', 'Mutant MCPE', '生存战争2', '无尽之路',
                     'Kick The buddy game run', 'Is-it Love ? Drogo : Vampire', '模拟火车', '奔跑吧，香肠', '干物少女', '云裳羽衣',
                     'MOD Spider Man MCPE', 'Defender Robot Mod for MCPE', '3D少女模拟', '小猪佩奇：假期', '模拟农场14完美版', '战士的游戏',
                     '爸爸的冷饮店', '妈妈把我的泡面藏起来了2', '小猪佩奇环游世界', '芭比公主化妆沙龙', '模拟农场18', '电子鼓垫免费',
                     'Black fire Dragon Mod for MCPE', '妈妈把我的辣条藏起来了 - 密室逃脱类游戏', '托卡小厨房寿司', '禁止作弊！', '校园女生模拟器',
                     'Scrap Mechanic guide New', '兰德里纳河的地下室', '小猪模拟器', '樱花校园模拟器', '小猪佩奇：圣诞愿望', '城市岛屿3：模拟城市', 'VR夜视模拟器',
                     '小猪佩奇：联欢会', 'Inventory guns mod for mcpe', '病娇模拟器', '我只是想上个厕所', '作弊不要被老师发现',
                     'Teleport Finger Simulator', '元气满满', 'Tips For Roblox Scary Elevator New', '文明时代', '王国保卫战：起源',
                     '托卡生活：办公室', '甜蜜合租间', '面具小飞侠', '农场小镇', '校园恋爱日记:甜蜜初恋', '自动售货机永恒的乐趣', '墨西哥高校模拟器2018', '购物女达人', '拘束少女',
                     'PUBG Quiz Mobile', '可口的披萨,美味的披萨', '笨蛋推理', '小猪佩奇：金色靴子', '生存战争', '喝鸡尾酒真正的Sim卡', '小猪佩奇拼图',
                     '天空女神——空姐', '飞杰DIY煤泥模拟器', '蘑菇花园', 'Grandpa - The Horror Game', 'Tutorial Scrap Mechanic'],
            '网络游戏': ['王者荣耀', '明日之后', '我的世界', '部落冲突Clash-of-Clans', '穿越火线：枪战王者', '侍魂：胧月传说', '绝地战场', '火影忍者OL',
                     '境·界-魂之觉醒（死神）', '明日之后（iOS同服版）', '航海王：燃烧意志', '部落冲突:皇室战争', '火影忍者', '英魂之刃', '我的孩子：生命之泉（中文试玩版）',
                     '炉石传说', '三国杀移动版', '崩坏3', '放置奇兵', '赛尔号星球大战', '光明勇士', '奥特曼英雄归来', '创造与魔法', '斗破苍穹：斗帝之路', '海岛奇兵',
                     '光荣使命：使命行动', '蜘蛛侠', '决战！平安京', '保卫萝卜3', '舌尖上的美食梦', '楚留香', '神都夜行录', '斗兽战棋', '红警OL', '疯狂动物园',
                     '模拟人生完美版', '我叫MT4', '300大作战', '口袋妖怪日月', '恋与制作人', '小兵大冲锋', '梦幻模拟战', '非人学园', '阿瑞斯病毒', '流星蝴蝶剑',
                     '阿拉德之怒', '极品芝麻官', '乐高我的岛屿创造', '敢达争锋对决', '天龙八部手游', '扭扭童年收集册', '择天记', '圣斗士星矢（腾讯）', '自由幻想',
                     '地下城堡2:黑暗觉醒', '野蛮人大作战', '火柴人联盟2', '探索大工艺', '梦幻西游', '漫威：未来之战', '时空召唤', '螺旋圆舞曲', '大掌门2', '全民超神-手机开黑',
                     '指挥官：军团守卫', '境界-死神激斗', '仙剑奇侠传4手游', '模拟城市3D', '永远的7日之都', '全民突击', '口袋妖怪：龙炎之心', '造梦西游OL', '银河掠夺者',
                     '火车模拟', '妖神记', '小米超神', '星辰奇缘', '月圆之夜', '王者传奇', '电击文库：零境交错', '我的方块世界', '口袋联盟', '猜我是谁', '造梦西游4',
                     '三国志2017', '战玲珑', '京剧猫', '剑侠情缘移动版', '奥特曼系列OL', '奇葩战斗家', '旅游巴士司机3D', '狼人杀', '孤岛先锋', '队长小翼：最强十一人',
                     '十万个冷笑话', '超级英雄机器人', '战争艺术', '倩女幽魂'],
            '体育竞技': ['实况足球', '最强NBA', 'NBA LIVE', 'FIFA足球世界', '街头篮球', '滑雪大冒险', '火柴人足球', '腾讯桌球', '8球台球', '羽毛球高高手',
                     '3D台球专业版', '台球大师专业版', '实况足球2013', '虚拟乒乓球 Virtual Tab...', '我的NBA2K16', 'NBA篮球大师', '潮人篮球',
                     '3D乒乓球 完整版', '火柴人足球2016', '热血足球', '桌球（单机版）', 'Guide Beyblade Tricks', '足球之王', '保龄球', '碰撞大作战',
                     'Spin Blade', '荒野狩猎', '台球大师', '真实滑板', '射箭 弩 比赛', '摔跤革命3D', '火柴人网球', '滑板', '狂热篮球', '冠军网球',
                     '胜利足球2014', '3D水滑梯', '全民冠军足球', '魔幻迷宫 3D', '射箭大比赛', '实况足球2014', 'News WWE Wrestling 2k17',
                     'NEW WWE 2K17 GUIDE', '弹弓锦标赛', '射击之王', '滑板派对', '水 冲浪 游泳 免费', '豪门足球风云', '虚拟乒乓', '逗比足球', '翻转跳水',
                     '双人足球:Soccer', '街篮', '真实击剑游戏', '街头篮球 - China version', '模拟篮球', '狂热篮球', '梦幻足球联盟', '台球帝国', '保龄球',
                     '赛马:赢得杯赛挑战', '桌面光球', '特技演员挑战赛', '自行车男孩', '3D网球大赛', '真实篮球 Real Basketball', '五人制足球联赛',
                     'Wrestling: WWE Smackdown News', '专业斯诺克2012', 'Athletics Running Race', 'PES 18', '终极足球',
                     '平衡板冲浪3D - Hoverboard Surfers', '拳击之王', 'Dream League Soccer 11', '冰球',
                     '胜利足球进化:Winner Soccer Evolution', '王牌NBA', '魔幻陀螺之飓风战魂', '拳击梦想', '摔角冠军', '激流快艇2小旗版', '火柴人羽毛球',
                     '傀儡足球2014', 'Score! Hero', '足球经理2018', '乒乓球大师', '夏季奥运会之田径项目 Athletics Summer Sports',
                     'NEW Tricks For Beyblade Burst', '百米赛跑', '世界乒乓球赛', '欢乐桌球', '实况足球 10pes6', '弓箭手世界杯2', '打篮球箍2015年',
                     '超级乒乓球', 'New WWE 2K18 Tricks', '平衡成球3D', 'NBA 2K14 辅助器 MyNBA2K14', '踢足球Soccer Kick', '篮球明星',
                     '国际斯诺克2', 'FIFA世界足球12HD', 'NBA范特西', '实况足球2008', 'FIFA 18 Mobile Soccer', 'PES 2017 3d', '足球',
                     '世界保龄球锦标赛', '指南：梦幻足球联赛17', '滑雪板盛宴2', '魅影车手'],
            '角色扮演': ['第五人格', '王者荣耀体验服', '口袋新世代', '口袋妖怪-绿宝石', '魂武者', '阴阳师', '奇迹MU：觉醒', '火影忍者疾风传-究极冲击', '口袋妖怪新白金光',
                     '口袋妖怪 白金', '虚荣', '口袋妖怪钻石', '天书奇谈', '时空猎人', '超能战队', '小花仙守护天使', '萌宠大作战', '仙灵外传', '赛尔号', '金庸群侠传X完美版',
                     '口袋妖怪：极光石', '轩辕传奇', '魔力宝贝', '热血传奇手机版', '梦幻诛仙手游', '口袋妖怪：混沌传说', '去吧皮卡丘', '口袋妖怪 绿叶版', '火柴人龙珠格斗',
                     '崩坏学园2', '玩具熊的五夜后宫4', '华夏', '三国大时代4霸王立志', '桃源仙境', '口袋妖怪暗兽神', '所谓侠客', '口袋妖怪叶绿', '贪玩蓝月', '口袋妖怪暗黑水银',
                     '魔塔50层勇者的试炼', '口袋妖怪：心魂之羽', '简仙', '黑暗传说单机RPG', '魔灵召唤：天空之役', '小冰冰传奇', '机战王', '精灵宝可梦进化', '问道',
                     '最终幻想7', '新口袋妖怪GT', '女神联盟2', '我的口袋妖怪世界', '传奇单机新版', '喵星人大战', '黎明三國', '战斗吧！精灵', '狐妖小红娘', '御龙在天',
                     '我的世界空岛大战', '龙珠激斗', '合金装备OPS', '小小妖怪', '山海经3D', '汉家江湖', 'BEN10终极英雄', '山海异闻录', '艾诺迪亚3：卡尼亚传人',
                     '口袋妖怪：TopEnding', '神奇宝贝ol', '皮卡丘超进化', '传奇世界', '枪神默示录', '王子的契约恋人【免费恋爱游戏】', '梦幻怪兽', '斗龙战士4双龙核之战',
                     '修仙传', '少年三国志', '放置江湖', '魔域口袋版', '末剑', '口袋妖怪：白金', '口袋妖怪-萌娘进化', '风流少侠', '进击的神奇宝贝', '火焰纹章 圣魔光石',
                     'Ben10 终极英雄', '火焰纹章 新暗黑龙与光之剑', '2047', '心灵战争', '金古群侠传', '宠物小精灵GO(S服版)', '神奇精灵', '桃花源记',
                     '混沌与秩序 Online国际安卓版', '我在大清当皇帝', '仙凡幻想', 'Guide for Pokemon GO Beta 2017', '欧陆战争4：拿破仑', '新三国小镇',
                     '秦时明月', '一剑情缘', '方舟指令', '航海王-启航', "Tricks Assassin's Creed Brotherhood", '单机三国志3', '宠物小精灵挂机版',
                     '破劫成仙'],
            '辅助工具': ['好游快爆', 'biubiu加速器', '九游游戏中心', '掌上英雄联盟', 'QQ游戏', '免Root叉叉助手', '软天空', '掌上穿越火线', '游大师', '电子鼓垫免费',
                     'Guide for Clash Of Clans', 'PSP模拟器', '爱游穿梭机', 'PSSP模拟器和PlayStation', 'GBA模拟器 My Boy!', '炉石传说掌游宝',
                     '旅法师营地', '实车驾驶', '17173游鲤', '逆战助手', '泰拉瑞亚盒子', 'GTA罪恶秘籍', 'GTA4策略', '女高中生校园逃脱', '部落战争助手', '我的世界合成表',
                     'GTA 4指南', 'LOL掌游宝', '圣安地列斯秘籍', 'Plants vs Zombies Easy Guide', '游戏键盘[安智汉化]', '8868手游交易',
                     '皇室战争幽灵辅助', '虚拟枪应用武器', 'GTA 4秘籍', '侠盗秘籍 GTA V - Guide Codes Astuces', '吉里吉里2模拟器', '5253', '口袋梦三国',
                     'G家', 'ePSXe PS模拟器', 'Best Flash Player Tricks', '天刀助手', '我的GBA模拟器免费版', '麦块我的世界盒子',
                     'GTA V / 5的汽车名单', 'Top WWE Fight with Tricks', '指尖架子鼓', '生存战争盒子',
                     'Unlimited Gems For Clash OF Clans Prank!', '手枪实景射击', 'MAME安卓模拟器', 'Kingo Root',
                     'Red Towers Open Beta', 'Ultimate Nes Emulator Pro', 'PlayStation游戏资讯', 'PS2 的 PSX 模拟器',
                     '反恐精英1.6客户端CS16Client', '疯狂砸电脑', '碉堡神器', 'PSP和模拟器高清游戏的Android和PlayStation', '游戏存档', '城市公交车驾驶3D模拟器',
                     '天堂模拟器', '建筑物拆除', 'NES 模拟器', '泰拉瑞亚攻略助手', 'Crash Test Iphone 8', '小皮手游宝', 'Minecraft皮肤偷取器', '偷窃钻石',
                     'Free NES Emulator', 'Police Jail Break', '超級NES模擬器', 'Simulátor řízení auta pro děti', 'VR Games',
                     '伏魔记', '泰拉瑞亚合成表大全', '连尚头条', '手机大亨', 'Polaroid PL2400', '超任模拟器汉化版', '炉石传说助手',
                     'Emulator GBA and GBC 2018 Free', 'NDS模拟器', 'Golden Psp和模拟器高清游戏的Android和PlayStation', 'OVERWATCH',
                     'Emulator for psp pro 2018', '手游视界', 'Guide LEGO DC Super Heroes', 'Cheat clash of clans - guide',
                     'Whack Your Computer', 'GBA模拟器:GBA.emu', 'TT stripping']}
    df = pd.DataFrame(name)
    print(df.head())
