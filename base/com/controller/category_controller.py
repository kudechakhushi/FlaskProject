from flask import request, render_template, redirect

from base import app
from base.com.controller.login_controller import login_required
from base.com.dao.category_dao import CategoryDAO
from base.com.vo.category_vo import CategoryVO


@app.route('/admin/load_category')
@login_required('admin')
def admin_load_category():
    try:
        return render_template('admin/addCategory.html')
    except Exception as ex:
        print("admin_load_category route exception occured>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)


@app.route('/admin/insert_category', methods=['POST'])
@login_required('admin')
def admin_insert_category():
    try:
        category_name = request.form.get('categoryName')
        category_description = request.form.get('categoryDescription')

        category_vo = CategoryVO()
        category_dao = CategoryDAO()

        category_vo.category_name = category_name
        category_vo.category_description = category_description

        category_dao.insert_category(category_vo)

        return redirect('/admin/view_category')
    except Exception as ex:
        print("admin_insert_category route exception occured>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)


@app.route('/admin/view_category')
@login_required('admin')
def admin_view_category():
    try:
        category_dao = CategoryDAO()
        category_vo_list = category_dao.view_category()
        return render_template('admin/viewCategory.html',
                               category_vo_list=category_vo_list)

    except Exception as ex:
        print("admin_view_category route exception occured>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)


@app.route('/admin/delete_category')
@login_required('admin')
def admin_delete_category():
    try:
        category_vo = CategoryVO()
        category_dao = CategoryDAO()
        category_id = request.args.get('categoryId')
        category_vo.category_id = category_id
        category_dao.delete_category(category_vo)
        return redirect('/admin/view_category')
    except Exception as ex:
        print("admin_delete_category route exception occured>>>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)


@app.route('/admin/edit_category', methods=['GET'])
@login_required('admin')
def admin_edit_category():
    try:
        category_vo = CategoryVO()
        category_dao = CategoryDAO()

        category_id = request.args.get('categoryId')
        category_vo.category_id = category_id
        category_vo_list = category_dao.edit_category(category_vo)
        return render_template('admin/editCategory.html',
                               category_vo_list=category_vo_list)
    except Exception as ex:
        print("admin_edit_category route exception occured>>>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)


@app.route('/admin/update_category', methods=['POST'])
@login_required('admin')
def admin_update_category():
    try:
        category_id = request.form.get('categoryId')
        category_name = request.form.get('categoryName')
        category_description = request.form.get('categoryDescription')

        category_vo = CategoryVO()
        category_dao = CategoryDAO()

        category_vo.category_id = category_id
        category_vo.category_name = category_name
        category_vo.category_description = category_description
        category_dao.update_category(category_vo)
        return redirect('/admin/view_category')
    except Exception as ex:
        print("admin_update_category route exception occured>>>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)
