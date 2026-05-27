from pages.add_remove_page import AddRemoveElementsPage


def test_add_remove_elements_pom(page, settings):
    ar = AddRemoveElementsPage(page).goto(settings["add_remove_url"])

    ar.add_elements(3)
    ar.expect_delete_count(3)

    ar.delete_by_index(0)
    ar.expect_delete_count(2)

    ar.delete_all()
    ar.expect_delete_count(0)