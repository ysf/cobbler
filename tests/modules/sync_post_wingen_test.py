from cobbler.modules import sync_post_wingen


def test_register():
    # Arrange & Act
    result = sync_post_wingen.register()

    # Assert
    assert result == "/var/lib/cobbler/triggers/sync/post/*"


def test_run():
    # Arrange
    args = None

    # Act
    result = sync_post_wingen.run(None, args)

    # Assert
    assert result
