from cobbler.modules import nsupdate_delete_system_pre


def test_register():
    # Arrange & Act
    result = nsupdate_delete_system_pre.register()

    # Assert
    assert result == "/var/lib/cobbler/triggers/add/system/post/*"


def test_run():
    # Arrange
    args = None

    # Act
    result = nsupdate_delete_system_pre.run(None, args)

    # Assert
    assert result
