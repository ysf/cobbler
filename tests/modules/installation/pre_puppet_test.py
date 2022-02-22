from cobbler.modules.installation import pre_puppet


def test_register():
    # Arrange & Act
    result = pre_puppet.register()

    # Assert
    assert result == "/var/lib/cobbler/triggers/install/pre/*"


def test_run():
    # Arrange
    args = None

    # Act
    result = pre_puppet.run(None, args)

    # Assert
    assert result
