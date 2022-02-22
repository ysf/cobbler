from cobbler.modules import scm_track


def test_register():
    # Arrange & Act
    result = scm_track.register()

    # Assert
    assert result == "/var/lib/cobbler/triggers/change/*"


def test_run():
    # Arrange
    args = None

    # Act
    result = scm_track.run(None, args)

    # Assert
    assert result
