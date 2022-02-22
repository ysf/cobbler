from cobbler.modules import sync_post_restart_services


def test_register():
    # Arrange & Act
    result = sync_post_restart_services.register()

    # Assert
    assert result == "/var/lib/cobbler/triggers/sync/post/*"


def test_run():
    # Arrange
    args = None

    # Act
    result = sync_post_restart_services.run(None, args)

    # Assert
    assert result
