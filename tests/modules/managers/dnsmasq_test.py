from cobbler.modules.managers import dnsmasq


def test_register():
    # Arrange & Act
    result = dnsmasq.register()

    # Assert
    assert result == "manage"


def test_manager_what():
    # Arrange & Act & Assert
    assert dnsmasq._DnsmasqManager.what() == "dnsmasq"


def test_get_manager(collection_mgr_mock):
    # Arrange & Act
    result = dnsmasq.get_manager(collection_mgr_mock)

    # Assert
    isinstance(result, dnsmasq._DnsmasqManager)
