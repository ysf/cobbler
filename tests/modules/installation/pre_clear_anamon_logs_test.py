from cobbler.modules.installation import pre_clear_anamon_logs


def test_register():
    # Arrange & Act
    result = pre_clear_anamon_logs.register()

    # Assert
    assert result == "/var/lib/cobbler/triggers/install/pre/*"


def test_run():
    # Arrange
    args = None

    # Act
    result = pre_clear_anamon_logs.run(None, args)

    # Assert
    assert result
