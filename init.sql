create table user(
    uid         int     not null,   -- 用户id
    username    text    not null,   -- 用户名
    password    text    not null,   -- 密码
    usergroup   text    not null,   -- 用户组 0管理员 1注册用户 2实名用户
    qq          text,               -- qq
    phone       text,               -- 手机号
    avatar      text    not null,   -- 头像地址
    info        text,               -- 个人简介
    realname    text,               -- 实名
    primary key(uid)
);

create table project(
    pid         int     not null,   -- 项目id
    uid         int     not null,   -- 发起人id
    title       text    not null,   -- 标题
    abstract    text    not null,   -- 项目自述
    img         text    not null,   -- 标题图
    content     text    not null,   -- 我的项目
    why         text    not null,   -- 为何众筹
    map         text    not null,   -- 区位图
    timeline    text    not null,   -- 时间轴
    time        int     not null,   -- 结束时间（天）
    status      int     not null,   -- 状态 -1删除   0未发布   1审核中    2众筹中    3众筹结束
    team        text    not null,   -- 团队成员列表
    primary key(uid)
);

create table payback(
    pbid        int     not null,   -- 回报id
    pid         int     not null,   -- 对应的项目id
    day         int     not null,   -- 发放时间
    money       real    not null,   -- 对应的金额
    content     text    not null,   -- 回报内容
    people      int     not null,   -- 限定人数
    primary key(pbid)
);

create table money_log(
    mid         int     not null,   -- 资金交易id
    uid_from    int     not null,   -- 转出方
    uid_to      int     not null,   -- 转入方
    time        text    not null,   -- 交易时间
    money       real    not null,   -- 交易金额
    pid         text,               -- 如果是众筹的话，众筹项目的id
    primary key(mid)
);
