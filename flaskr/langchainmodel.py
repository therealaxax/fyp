from flask import Blueprint, flash, request, render_template, redirect, url_for
from FYP import sqlagentwithtools_module
from FYP import importdata
from FYP import dbsearch_module

bp = Blueprint('langchainmodel', __name__, url_prefix='/langchainmodel')

@bp.route('/input', methods=('GET', 'POST'))
def input():
    data = {"query": "empty", "response": "empty"}
    if request.method == 'POST':
        query = request.form['query']
        data["query"] = query
        # db = get_db()
        error = None

        if not query:
            error = 'Please enter a query.'

        if error is None:
            custom_tool_list = sqlagentwithtools_module.fewshots()
            custom_tool_list.append(sqlagentwithtools_module.propernounsearchtool())
            print(custom_tool_list)
            agent_executor = sqlagentwithtools_module.createsqlagentwithtools(custom_tool_list)
            # flash(agent_executor.run(query))
            # response = agent_executor.invoke(query)
            response = agent_executor.run(query)
            # flash(response)
            data["response"] = response
        else:
            return redirect(url_for("langchainmodel.input"))

    return render_template('langchainmodel/input.html', data=data)

@bp.route('/dataimportview', methods=('GET', 'POST'))
def dataimportview():
    if request.method == 'POST':
        error = None

        if error is None:
            flash(importdata.performimportdata())
            # return redirect(url_for("langchainmodel.importdata"))
        else:
            return redirect(url_for("langchainmodel.dataimportview"))

    return render_template('langchainmodel/dataimportview.html')

@bp.route('/fewshotsview', methods=('GET', 'POST'))
def fewshotsview():
    connection = dbsearch_module.create_connection("fewshots")
    data = {"propernouns": "empty", "fewshotexamplequery": "empty"}

    if request.method == 'POST':
        error = None

        if error is None:
            if request.form['fewshotexamplequestion'] != '' and request.form['fewshotexamplequery'] != '':
                dbsearch_module.insert_single_col_fewshots(connection, request.form['fewshotexamplequestion'], request.form['fewshotexamplequery'])
            if request.form['propernoun'] != '':
                dbsearch_module.insert_single_col_propernouns(connection, request.form['propernoun'])
            if request.form.get('displaynoun') == 'displaynounclicked':
                sql = "SELECT * FROM propernouns"
                flash("List of proper nouns displayed below.")
                # flash(dbsearch_module.select_query_list(sql, connection))
                data["propernouns"] = dbsearch_module.select_query_list(sql, connection)
            if request.form.get('displayfewshotexamplequery') == 'displayfewshotexamplequeryclicked':
                sql = "SELECT * FROM fewshotexamples"
                flash("Few shot question examples displayed below.")
                # flash(dbsearch_module.select_query_list(sql, connection))
                data["fewshotexamplequery"] = dbsearch_module.select_query_list(sql, connection)
        else:
            return redirect(url_for("langchainmodel.fewshotsview"))

    return render_template('langchainmodel/fewshotsview.html', data=data)