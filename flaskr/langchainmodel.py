from flask import Blueprint, flash, request, render_template
from FYP import sqlagentwithtools_module

bp = Blueprint('langchainmodel', __name__, url_prefix='/langchainmodel')

@bp.route('/input', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            custom_tool_list = sqlagentwithtools_module.fewshots()
            agent_executor = sqlagentwithtools_module.createsqlagentwithtools(custom_tool_list)
            flash(agent_executor.run("Which is the smallest army airfield by area?"))
        else:
            return redirect(url_for("langchainmodel.input"))

    return render_template('langchainmodel/input.html')