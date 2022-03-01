from cobbler.templar import Templar
from cobbler.modules.managers import genders


def test_register():
    # Arrange
    # Act
    result = genders.register()

    # Assert
    assert result == "/var/lib/cobbler/triggers/change/*"


def test_write_genders_file(mocker):
    # Arrange
    templar_mock = mocker.patch(Templar, autospec=True)
    # TODO: Create mock API
    # TODO: Create mock mgmtclasses
    # TODO: Create mock distros
    # TODO: Create mock profiles

    # Act
    result = genders.write_genders_file(None, None, None, None)

    # Assert
    assert templar_mock.render.call_count == 1
    templar_mock.render.assert_called_with("")


def test_run():
    # Arrange
    # TODO: Create mock API
    # TODO: Mock write_genders_file

    # Act
    result = genders.run(None, [])

    # Assert
    # TODO: Assert correct call to write_genders_file
    assert result == 0
