DROP database if EXISTS finacial_management;

create database finacial_management default charset utf8 collate utf8_general_ci;
use finacial_management;
# 用户表
DROP TABLE IF EXISTS `users`;
create table users(
    id varchar(50) not null COMMENT 'id',
    username varchar(50) not null COMMENT '用户名',
    passwd varchar(50) not null COMMENT '密码',
    email varchar(50) not null COMMENT '邮件',
    is_admin boolean not null COMMENT '是否是管理员',
    image varchar(500) COMMENT '用户头像',
    name varchar(50) COMMENT '用户姓名',
    created_at bigint(20) not null COMMENT '创建时间',
    primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='用户表';

# 记录表
DROP TABLE IF EXISTS `records`;
create table records(
    id varchar(50) not null COMMENT 'id',
    uid varchar(50) not null COMMENT '用户id',
    typeid varchar(50) not null COMMENT '类型id',
    tagid varchar(50) not null COMMENT '标签id',
    type boolean not null COMMENT '类型:0支出, 1收入',
    money double(10,2) not null COMMENT '金额',
    commnets varchar(200) COMMENT '备注',
    created_at bigint(20) not null COMMENT '创建时间',
    primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='记录表';

# 类型表
DROP TABLE IF EXISTS `types`;
create table types(
    id varchar(50) not null COMMENT 'id',
    name varchar(50) not null COMMENT '名称',
    orders bigint(3) not null COMMENT '顺序',
    created_at bigint(20) not null COMMENT '创建时间',
    primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='类型表';

# tags
DROP TABLE IF EXISTS `tags`;
create table tags(
    id varchar(50) not null COMMENT 'id',
    name varchar(50) not null COMMENT '名称',
    uid varchar(50) not null COMMENT '用户id',
    typeid varchar(50) not null COMMENT '类型id',
    created_at bigint(20) not null COMMENT '创建时间',
    primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='标签';