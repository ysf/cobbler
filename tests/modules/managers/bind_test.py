from cobbler.modules.managers import bind


def test_register():
    # Arrange & Act
    result = bind.register()

    # Assert
    assert result == "bind"


def test_manager_what():
    # Arrange & Act & Assert
    assert bind._BindManager.what() == "bind"


def test_get_manager(collection_mgr_mock):
    # Arrange & Act
    result = bind.get_manager(collection_mgr_mock)

    # Assert
    isinstance(result, bind._BindManager)
