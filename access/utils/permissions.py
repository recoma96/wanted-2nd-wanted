from core.miniframework_on_django.query_layer.access_query.permission import PermissionIssueChecker


class SignUpPermissionChecker(PermissionIssueChecker):
    issue = 'sign-up'