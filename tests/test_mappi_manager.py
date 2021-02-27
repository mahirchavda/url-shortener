import pytest

import const
import mappi_manager


nicknames = mappi_manager.MappiManager.load_nickname(const.NICKNAME_FILE)


jira_ticket = "{jira}/browse/{{jira_id}}".format(**nicknames)
jira_other = "{jira}/{{other}}".format(**nicknames)

confluence_project = "{confluence}/display/PROJ/{{project}}".format(**nicknames)
confluence_query = "{confluence}/dosearchsite.action?queryString={{query}}".format(
    **nicknames
)

bibucket_repo_search = "{bitbucket}/dashboard/repositories?search={{query}}".format(
    **nicknames
)
bibucket_code_search = "{bitbucket}/search?q={{query}}".format(**nicknames)


@pytest.mark.parametrize(
    "short_url, expected_redirect_url",
    [
        # jira
        ("/j", nicknames["jira"]),
        ("/J/", nicknames["jira"]),
        ("/jira", nicknames["jira"]),
        ("/JIRA", nicknames["jira"]),
        ("/JiRa/", nicknames["jira"]),
        (
            "/timeshit",
            jira_other.format(other="plugins/servlet/aio-ts/bridge/pages/aiotimeentry"),
        ),
        (
            "/timesheet",
            jira_other.format(other="plugins/servlet/aio-ts/bridge/pages/aiotimeentry"),
        ),
        ("/j/PROJ1-1", jira_ticket.format(jira_id="PROJ1-1")),
        ("/J/PROJ2-1012", jira_ticket.format(jira_id="PROJ2-1012")),
        # confluence
        ("/c", nicknames["confluence"]),
        ("/c/project1", confluence_project.format(project="project1")),
        (
            "/confluence/Hello how are you?",
            confluence_query.format(query="Hello how are you?"),
        ),
        # bitbucket
        ("/bb", nicknames["bitbucket"]),
        ("/bitbucket", nicknames["bitbucket"]),
        (
            "/bitbucket/url-shortener",
            bibucket_repo_search.format(query="url-shortener"),
        ),
        (
            "/bitbucket/code/python.version",
            bibucket_code_search.format(query="python.version"),
        ),
    ],
)
def test_get_redirect_url(mappi_man, short_url, expected_redirect_url):
    assert mappi_man.get_redirect_url(short_url) == expected_redirect_url
