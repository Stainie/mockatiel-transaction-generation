from . import bp

@bp.app_errorhandler(404)
def page_not_found(e):
    return "404 Not Found"

@bp.app_errorhandler(500)
def internal_server_error(e):
    return "500 Internal Server Error"