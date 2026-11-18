from pages.localhost.userspage import UsersPage
from pages.localhost.tenantspage import TenantsPage
import pytest

@pytest.mark.parametrize('creds', ['admin'], indirect=True)
@pytest.mark.parametrize('page_url', ['tenants'], indirect=True)
def test_localhost_tenants_page(logged_in_page, page_url, creds):
    logged_in_page.get(page_url)

    tenants_page = TenantsPage(logged_in_page)
    tenants_page.check_tenant_page_title('h2', 'Отделы')
    tenants_page.check_tenant_info('.tenant-name', 'Отдел бухгалтерии')
    tenants_page.click_tenant_detail_btn('''//*[@class='base-button base-button--secondary details-button'][1]''')
    tenants_page.check_header_tag_text('h2', 'Отдел бухгалтерии')
    tenants_page.check_header_title_and_value('Отдел бухгалтерии', 'Всего сотрудников: 1')

@pytest.mark.parametrize('creds', ['user3'], indirect=True)
@pytest.mark.parametrize('page_url', ['users'], indirect=True)
def test_localhost_users_page(logged_in_page, page_url, creds):
    logged_in_page.get(page_url)
    users_page = UsersPage(logged_in_page)
    users_page.click_user_profile('''//ul[@class='users-list']/li[@class='user-card'][1]/div[@class='user-actions']/button''')
    users_page.check_user_profile_field("Логин:", "user2")



