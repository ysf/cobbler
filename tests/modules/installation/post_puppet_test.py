from cobbler.modules.installation import post_puppet


def test_register():
    # Arrange & Act
    result = post_puppet.register()

    # Assert
    assert result == "/var/lib/cobbler/triggers/install/post/*"


def test_run():
    # Arrange
    args = None

    # Act
    result = post_puppet.run(None, args)

    # Assert
    assert result
