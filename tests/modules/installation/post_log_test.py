from cobbler.modules.installation import post_log


def test_register():
    # Arrange & Act
    result = post_log.register()

    # Assert
    assert result == "/var/lib/cobbler/triggers/install/post/*"


def test_run():
    # Arrange
    args = None

    # Act
    result = post_log.run(None, args)

    # Assert
    assert result
