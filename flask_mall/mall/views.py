from flask import Blueprint, request, render_template, flash, redirect, abort, url_for
from forms import ProductEditForm
from models import Product, db

mall = Blueprint('mall',__name__,template_folder='templates',static_folder='static')


@mall.route('/product/list/<int:page>')
# @login_required     # 建议使用flask-login
def product_list(page):
    """商品列表"""
    page_size = 2   # 每页2条
    # 查询搜索条件的查询
    name = request.args.get('name','')
    # print('name---',name)
    if name:
        page_data = Product.query.filter(Product.name.contains(name),Product.is_valid == True).paginate(page=page,per_page=page_size)
    else:
        page_data = Product.query.filter(Product.is_valid==True).paginate(page=page,per_page=page_size)
        # print(page_data.items)
    return render_template('product_list.html',page_data=page_data)


@mall.route('/product/detail/<uid>')
def product_detail(uid):
    """商品详情"""
    # 如果触发404，定制404界面
    prod_obj = Product.query.filter_by(uid=uid).first_or_404()
    # print(prod_obj)
    return render_template('product_detail.html',prod_obj=prod_obj)


@mall.route('/product/add',methods=['POST','GET'])
def product_add():
    """商品添加"""
    form = ProductEditForm()
    if form.validate_on_submit():
        # 保存到数据库
        # print(form.data)
        prod_obj = Product(
            name=form.data['name'],
            content=form.data['content'],
            desc=form.data['desc'],
            types=form.data['types'],
            price=form.data['price'],
            origin_price=form.data['origin_price'],
            img='/xxx.jpg',
            channel=form.data['channel'],
            buy_link=form.data['buy_link'],
            status=form.data['status'],
            sku_count=form.data['sku_count'],
            remain_count=form.data['remain_count'],
            view_count=form.data['view_count'],
            score=form.data['score'],

            is_valid=form.data['is_valid'],
            reorder=form.data['reorder'])
        db.session.add(prod_obj)
        db.session.commit()
        # 产生一个消息闪现提示
        flash('新增商品成功', 'success')
        # 跳转到商品列表中
        return redirect(url_for('mall.product_list',page=1))
    else:
        flash('请新增商品，然后提交','warning')  # 产生一个消息闪现提示
        # print(form.errors)
    return render_template('product_add.html',form=form)


@mall.route('/product/edit/<uid>',methods=['POST','GET'])
def product_edit(uid):
    """商品编辑"""
    prod_obj = Product.query.filter_by(uid=uid,is_valid=True).first()
    print(prod_obj)
    if prod_obj is None:
        abort(404)
    form = ProductEditForm(obj=prod_obj)
    if form.validate_on_submit():
        prod_obj.name = form.data['name']
        prod_obj.content = form.data['content']
        prod_obj.desc = form.data['desc']
        prod_obj.types = form.data['types']
        prod_obj.price = form.data['price']
        prod_obj.origin_price = form.data['origin_price']
        prod_obj.img = '/xxx.jpg'
        prod_obj.channel = form.data['channel']
        prod_obj.buy_link = form.data['buy_link']
        prod_obj.status = form.data['status']
        prod_obj.sku_count = form.data['sku_count']
        prod_obj.remain_count = form.data['remain_count']
        prod_obj.view_count = form.data['view_count']
        prod_obj.score = form.data['score']
        prod_obj.is_valid = form.data['is_valid']
        prod_obj.reorder = form.data['reorder']
        db.session.add(prod_obj)
        db.session.commit()
        flash('修改成功','success')
        return redirect(url_for('mall.product_list',page=1))
    else:
        print(form.errors)
    return render_template('product_edit.html',form=form,prod_obj=prod_obj)


@mall.route('/product/delete/<uid>',methods=['GET','POST'])
def product_delete(uid):
    """商品的删除"""
    prod_obj = Product.query.filter_by(uid=uid,is_valid=True).first()
    if prod_obj is None:
        return 'no'
    prod_obj.is_valid = False
    db.session.add(prod_obj)
    db.session.commit()
    return 'ok'
