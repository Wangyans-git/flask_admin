import uuid

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """用户模型"""
    __tablename__ = 'accounts_user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    nickname = db.Column(db.String(64))

    is_valid = db.Column(db.Boolean, default=True)
    is_super = db.Column(db.Boolean, default=False)


class Tag(db.Model):
    """商品标签"""
    __tablename__ = 'product_tag'
    # 主键
    id = db.Column(db.Integer,primary_key=True)
    # UID
    uid=db.Column(db.String(128),nullable=False,default=uuid.uuid4,unique=True)
    # 标签名称
    name=db.Column(db.String(128),nullable=False)
    # 标签编码
    code=db.Column(db.String(32))
    # 标签的描述
    desc=db.Column(db.String(256))
    # 逻辑删除
    is_valid=db.Column(db.Boolean,default=True)
    # 排序
    reorder=db.Column(db.Integer,default=0)
    # 创建的时间
    created_at=db.Column(db.DateTime)
    # 最后修改的时间
    update_at=db.Column(db.DateTime)


class Classify(db.Model):
    """商品分类"""
    __tablename__='product_classify'
    # 主键
    id=db.Column(db.Integer, primary_key=True)
    # UID
    uid=db.Column(db.String(128), nullable=False, default=uuid.uuid4, unique=True)
    # 关联父级的ID
    parent_id=db.Column(db.Integer,db.ForeignKey('product_classify.id'))
    # 分类图片的地址
    img=db.Column(db.String(256))
    # 分类名称
    name=db.Column(db.String(128), nullable=False)
    # 分类编码
    code=db.Column(db.String(32))
    # 分类的描述
    desc=db.Column(db.String(256))
    # 逻辑删除
    is_valid=db.Column(db.Boolean, default=True)
    # 排序
    reorder=db.Column(db.Integer, default=0)
    # 创建的时间
    created_at=db.Column(db.DateTime)
    # 最后修改的时间
    update_at=db.Column(db.DateTime)


class Product(db.Model):
    """商品"""
    __tablename__='product'
    # 主键
    id=db.Column(db.Integer, primary_key=True)
    # UID
    uid=db.Column(db.String(128), nullable=False, default=uuid.uuid4, unique=True)
    # 商品标题
    name=db.Column(db.String(128),nullable=False)
    # 商品描述（富文本）
    content=db.Column(db.Text,nullable=False)
    # 商品简述（推荐语）
    desc=db.Column(db.String(256))
    # 类型
    types=db.Column(db.String(10),nullable=False)
    # 价格
    price=db.Column(db.Integer,nullable=False)
    # 原价
    origin_price=db.Column(db.Float)
    # 主图
    img=db.Column(db.String(256),nullable=False)
    # 渠道
    channel=db.Column(db.String(32))
    # 链接
    buy_link=db.Column(db.String(256))
    # 商品状态
    status=db.Column(db.String(10),nullable=False)
    # 库存
    sku_count=db.Column(db.Integer,default=0)
    # 剩余库存
    remain_count=db.Column(db.Integer,default=0)
    # 浏览次数
    view_count=db.Column(db.Integer,default=0)
    # 评分
    score=db.Column(db.Float,default=10)

    # 逻辑删除
    is_valid=db.Column(db.Boolean, default=True)
    # 排序
    reorder=db.Column(db.Integer, default=0)
    # 创建的时间
    created_at=db.Column(db.DateTime)
    # 最后修改的时间
    update_at=db.Column(db.DateTime)


class ProductClasses(db.Model):
    """商品与分类的关系"""
    __tablename__='product_classify_rel'

    # 主键
    id=db.Column(db.Integer, primary_key=True)

    product_id=db.Column(db.Integer,db.ForeignKey('product.id'))
    cls_id=db.Column(db.Integer,db.ForeignKey('product_classify.id'))


class ProductTags(db.Model):
    """商品与标签的关系"""
    __tablename__='product_tag_rel'

    # 主键
    id = db.Column(db.Integer, primary_key=True)

    product_id=db.Column(db.Integer, db.ForeignKey('product.id'))
    tag_id=db.Column(db.Integer, db.ForeignKey('product_tag.id'))