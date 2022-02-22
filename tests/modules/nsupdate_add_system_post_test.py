from cobbler.modules import nsupdate_add_system_post


def test_register():
    # Arrange & Act
    result = nsupdate_add_system_post.register()

    # Assert
    assert result == "/var/lib/cobbler/triggers/add/system/post/*"


def test_run():
    # Arrange
    args = None

    # Act
    result = nsupdate_add_system_post.run(None, args)

    # Assert
    assert result
