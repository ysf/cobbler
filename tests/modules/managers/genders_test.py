from cobbler.modules.managers import genders


def test_register():
    # Arrange
    # Act
    result = genders.register()

    # Assert
    assert result == "/var/lib/cobbler/triggers/change/*"


def test_write_genders_file():
    # Arrange
    # Act
    result = genders.write_genders_file()

    # Assert
    assert False


def test_run():
    # Arrange
    # Act
    result = genders.run()

    # Assert
    assert False
