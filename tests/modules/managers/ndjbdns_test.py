from cobbler.modules.managers import ndjbdns


def test_register():
    # Arrange
    # Act
    result = ndjbdns.register()

    # Assert
    assert result == "manage"


def test_get_manager(collection_mgr_mock):
    # Arrange & Act
    result = ndjbdns.get_manager(collection_mgr_mock)

    # Assert
    isinstance(result, ndjbdns._NDjbDnsManager)


def test_manager_what():
    # Arrange & Act & Assert
    assert ndjbdns._NDjbDnsManager.what() == "ndjbdns"
