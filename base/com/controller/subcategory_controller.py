from flask import request, render_template, redirect, url_for

from base import app
from base.com.controller.login_controller import login_required
from base.com.dao.category_dao import CategoryDAO
from base.com.dao.subcategory_dao import SubCategoryDAO
from base.com.vo.subcategory_vo import SubCategoryVO


@app.route('/admin/load_subcategory')
@login_required('admin')
def admin_load_subcategory():
    try:
        category_dao = CategoryDAO()
        category_vo_list = category_dao.view_category()
        return render_template('admin/addSubcategory.html',
                               category_vo_list=category_vo_list)
    except Exception as ex:
        print("admin_load_subcategory route exception occured>>>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)


@app.route('/admin/insert_subcategory', methods=['POST'])
@login_required('admin')
def admin_insert_subcategory():
    try:
        subcategory_name = request.form.get('subCategoryName')
        subcategory_description = request.form.get(
            'subCategoryDescription')
        subcategory_category_id = request.form.get('subcategoryCategoryId')

        subcategory_vo = SubCategoryVO()
        subcategory_dao = SubCategoryDAO()

        subcategory_vo.subcategory_name = subcategory_name
        subcategory_vo.subcategory_description = subcategory_description
        subcategory_vo.subcategory_category_id = subcategory_category_id
        subcategory_dao.insert_subcategory(subcategory_vo)
        return redirect(url_for('admin_view_subcategory'))
    except Exception as ex:
        print("admin_insert_subcategory route exception occured>>>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)


@app.route('/admin/view_subcategory')
@login_required('admin')
def admin_view_subcategory():
    try:
        subcategory_dao = SubCategoryDAO()
        subcategory_vo_list = subcategory_dao.view_subcategory()
        return render_template('admin/viewSubcategory.html',
                               subcategory_vo_list=subcategory_vo_list)
    except Exception as ex:
        print("admin_view_subcategory route exception occured>>>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)


@app.route('/admin/delete_subcategory')
@login_required('admin')
def admin_delete_subcategory():
    try:
        subcategory_dao = SubCategoryDAO()
        subcategory_id = request.args.get('subCategoryId')
        subcategory_dao.delete_subcategory(subcategory_id)
        return redirect(url_for('admin_view_subcategory'))
    except Exception as ex:
        print("admin_delete_subcategory route exception occured>>>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)


@app.route('/admin/edit_subcategory')
@login_required('admin')
def admin_edit_subcategory():
    try:
        subcategory_vo = SubCategoryVO()
        subcategory_dao = SubCategoryDAO()
        category_dao = CategoryDAO()

        subcategory_id = request.args.get('subCategoryId')
        subcategory_vo.subcategory_id = subcategory_id
        subcategory_vo_list = subcategory_dao.edit_subcategory(
            subcategory_vo)
        category_vo_list = category_dao.view_category()
        return render_template('admin/editSubcategory.html',
                               category_vo_list=category_vo_list,
                               subcategory_vo_list=subcategory_vo_list)
    except Exception as ex:
        print("admin_edit_subcategory route exception occured>>>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)


@app.route('/admin/update_subcategory', methods=['POST'])
@login_required('admin')
def admin_update_subcategory():
    try:
        subcategory_id = request.form.get('subCategoryId')
        subcategory_name = request.form.get('subCategoryName')
        subcategory_description = request.form.get(
            'subCategoryDescription')
        subcategory_category_id = request.form.get('subcategoryCategoryId')

        subcategory_vo = SubCategoryVO()
        subcategory_dao = SubCategoryDAO()

        subcategory_vo.subcategory_id = subcategory_id
        subcategory_vo.subcategory_name = subcategory_name
        subcategory_vo.subcategory_description = subcategory_description
        subcategory_vo.subcategory_category_id = subcategory_category_id
        subcategory_dao.update_subcategory(subcategory_vo)
        return redirect(url_for('admin_view_subcategory'))
    except Exception as ex:
        print("admin_update_subcategory route exception occured>>>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)
