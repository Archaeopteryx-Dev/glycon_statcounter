from django.template.loader import render_to_string


def statcounter_block_html(project_id):
    return render_to_string("statcounter.html", context={"project_id": project_id})