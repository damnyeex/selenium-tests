from pages.spring_app_pages.users_page import UsersPage
from pages.spring_app_pages.tenants_page import TenantsPage
import pytest

@pytest.mark.parametrize('creds', ['admin'], indirect=True)
@pytest.mark.parametrize('page_url', ['tenants'], indirect=True)
def test_localhost_tenants_page(logged_in_page, page_url, creds):
    logged_in_page.get(page_url)

    tenants_page = TenantsPage(logged_in_page)
    tenants_page.check_tenant_page_title('Отделы')
    tenants_page.check_tenant_info('Отдел бухгалтерии')
    tenants_page.click_tenant_detail_btn()
    tenants_page.check_header_tag_text('h2', 'Отдел бухгалтерии')
    tenants_page.check_header_title_and_value('Отдел бухгалтерии', 'Всего сотрудников: 1')

@pytest.mark.parametrize('creds', ['user3'], indirect=True)
@pytest.mark.parametrize('page_url', ['users'], indirect=True)
def test_localhost_users_page(logged_in_page, page_url, creds):
    logged_in_page.get(page_url)
    users_page = UsersPage(logged_in_page)
    users_page.click_user_profile()
    users_page.check_user_profile_field("Логин:", "user2")



