from cobbler.modules.installation import pre_log


def test_register():
    # Arrange & Act
    result = pre_log.register()

    # Assert
    assert result == "/var/lib/cobbler/triggers/install/pre/*"


def test_run():
    # Arrange
    args = []

    # Act
    result = pre_log.run(None, args)

    # Assert
    assert result
