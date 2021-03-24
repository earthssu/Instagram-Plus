from src import app, post_coll
from flask import request, url_for, redirect, render_template


# 메인 페이지
@app.route('/')
def index():
    post_list = post_coll.find({})
    return render_template('index.html', post=post_list)


# 검색 및 결과
@app.route('/result', methods=['POST'])
def search():
    do = request.form['do']
    dont = request.form['dont']
    post_list = post_coll.find({})
    result_list = []

    do_list = do.split(" ")
    print(do_list)
    dont_list = list()
    if dont != "":
        dont_list = dont.split(" ")
    print(dont_list)

    for post in post_list:
        tag = post['tag']
        if do in tag:
            if dont == "":
                result_list.append(post)
            elif dont not in tag:
                result_list.append(post)

    print(result_list)
    return render_template('result.html', post=result_list)



@app.route('/single')
def single():
    return render_template('single.html')