from flask import Blueprint,render_template,request,url_for,redirect,flash,abort
from users.form import RegistrationForm,Change_Form
from users.problem import Problem
from users import db
problems=Blueprint('problems',__name__)

@problems.route('/',methods=['GET'])
def frist():
    #立ち上げの初期表示
    return redirect(url_for('problems.all_memo'))

@problems.route('/add_memo',methods=['GET','POST'])
def add_memo():
    #メモを追加するview関数
    form=RegistrationForm()
    if form.validate_on_submit():
        problems=Problem(language=form.language.data,error_name=form.error_name.data,error_content=form.error_content.data)
        db.session.add(problems)
        db.session.commit()
        flash('メモが追加されました')
        return redirect(url_for('problems.all_memo'))
    return render_template('add_memo.html',form=form)

@problems.route('/all_memo',methods=['GET','POST'])
def all_memo():
    #メモを一覧表示するview関数
    page=request.args.get('page',1,type=int)
    problems=Problem.query.order_by(Problem.id).paginate(page=page,per_page=10)
    return render_template('all_memo.html',problems=problems)


@problems.route('/<int:change_id>/change_form',methods=['GET','POST'])
def change_form(change_id):
    #登録した情報を変更するview関数
    problem=Problem.query.get_or_404(change_id)
    form=Change_Form(change_id)
    if form.validate_on_submit():
        problem.language=form.language.data
        problem.error_name=form.error_name.data
        problem.error_content=form.error_content.data
        db.session.commit()
        flash('メモが更新されました')
        return redirect(url_for('problems.all_memo'))
    elif request.method=='GET':
        form.language.data=problem.language
        form.error_name.data=problem.error_name
        form.error_content.data=problem.error_content
    return render_template('change.html',form=form)


@problems.route('/<int:change_id>/delete_problems',methods=['GET','POST'])
def delete_problem(change_id):
    delete_problems=Problem.query.get_or_404(change_id)
    db.session.delete(delete_problems)
    db.session.commit()
    flash('選択したメモが削除されました')
    return redirect(url_for('problems.all_memo'))
