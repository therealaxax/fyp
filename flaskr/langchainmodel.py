from flask import Blueprint, flash, request, render_template, redirect, url_for
from FYP import sqlagentwithtools_module
from FYP import importdata

bp = Blueprint('langchainmodel', __name__, url_prefix='/langchainmodel')

@bp.route('/input', methods=('GET', 'POST'))
def input():
    if request.method == 'POST':
        query = request.form['query']
        # db = get_db()
        error = None

        if not query:
            error = 'Please enter a query.'

        if error is None:
            custom_tool_list = sqlagentwithtools_module.fewshots()
            agent_executor = sqlagentwithtools_module.createsqlagentwithtools(custom_tool_list)
            flash(agent_executor.run(query))
        else:
            return redirect(url_for("langchainmodel.input"))

    return render_template('langchainmodel/input.html')

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