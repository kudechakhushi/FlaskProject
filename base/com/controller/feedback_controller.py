import datetime

from flask import render_template, redirect, request, url_for
import jwt
from base import app
from base.com.controller.login_controller import login_required
from base.com.dao.feedback_dao import FeedbackDAO
from base.com.dao.login_dao import LoginDAO
from base.com.vo.feedback_vo import FeedbackVO
from base.com.vo.login_vo import LoginVO


@app.route('/admin/view_feedback')
@login_required('admin')
def admin_view_feedback():
    try:
        feedback_dao = FeedbackDAO()

        feedback_vo_list = feedback_dao.admin_view_feedback()
        return render_template('admin/viewFeedback.html',
                               feedback_vo_list=feedback_vo_list)
    except Exception as ex:
        print("admin_view_feedback route exception occured>>>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)


@app.route('/admin/delete_feedback')
@login_required('admin')
def admin_delete_feedback():
    try:
        feedback_dao = FeedbackDAO()
        feedback_vo = FeedbackVO()
        feedback_id = request.args.get('feedbackId')
        feedback_vo.feedback_id = feedback_id
        feedback_dao.delete_feedback(feedback_vo)
        return redirect(url_for('admin_view_feedback'))
    except Exception as ex:
        print("admin_delete_feedback route exception occured>>>>>>>>>>", ex)
        return render_template('admin/viewError.html', ex=ex)


@app.route('/user/insert_feedback', methods=['POST'])
@login_required('user')
def user_insert_feedback():
    try:
        feedback_rating = request.form.get('rating')
        feedback_description = request.form.get('feedbackDescription')
        feedback_date = datetime.datetime.now()

        feedback_dao = FeedbackDAO()
        feedback_vo = FeedbackVO()
        login_vo = LoginVO()
        login_dao = LoginDAO()

        refreshtoken = request.cookies.get('refreshtoken')

        data = jwt.decode(refreshtoken, app.config['SECRET_KEY'],
                          'HS256')
        login_vo.login_username = data['public_id']
        login_id = login_dao.find_login_id(login_vo)

        feedback_vo.feedback_description = feedback_description
        if feedback_rating:
            feedback_vo.feedback_rating = feedback_rating
        feedback_vo.feedback_datetime = feedback_date
        feedback_vo.feedback_login_id = login_id
        feedback_dao.insert_feedback(feedback_vo)
        return redirect(url_for('user_view_feedback'))
    except Exception as ex:
        print("user_insert_feedback route exception occured>>>>>>>>>>", ex)
        return render_template('user/viewError.html', ex=ex)


@app.route('/user/view_feedback')
@login_required('user')
def user_view_feedback():
    try:
        feedback_dao = FeedbackDAO()
        feedback_vo = FeedbackVO()
        login_vo = LoginVO()
        login_dao = LoginDAO()

        refreshtoken = request.cookies.get('refreshtoken')
        print("refreshtoken",refreshtoken)

        data = jwt.decode(refreshtoken, app.config['SECRET_KEY'],
                          'HS256')
        print("data",data)
        login_vo.login_username = data['public_id']
        login_id = login_dao.find_login_id(login_vo)
        print("login_id",login_id)
        feedback_vo.feedback_login_id = login_id

        feedback_vo_list = feedback_dao.user_view_feedback(feedback_vo)
        print("feedback_vo_list",feedback_vo_list)
        return render_template("user/addFeedback.html",
                               feedback_vo_list=feedback_vo_list)
    except Exception as ex:
        print("user_view_feedback route exception occured>>>>>>>>>>", ex)
        return render_template('user/viewError.html', ex=ex)
