from unittest.mock import Mock

import pytest

from cobbler.modules.managers import in_tftpd


def test_register():
    # Arrange
    # Act
    result = in_tftpd.register()

    # Assert
    assert result == "manage"


def test_manager_what():
    # Arrange & Act & Assert
    assert in_tftpd._InTftpdManager.what() == "in_tftpd"


def test_tftpd_singleton():
    # Arrange
    mcollection = Mock()

    # Act
    manager_1 = in_tftpd.get_manager(mcollection)
    manager_2 = in_tftpd.get_manager(mcollection)

    # Assert
    assert manager_1 == manager_2


def test_manager_write_boot_files_distro():
    # Arrange
    manager_obj = in_tftpd.get_manager(None)

    # Act
    manager_obj.write_boot_files_distro(None)

    # Assert
    assert False


def test_manager_write_boot_files():
    # Arrange
    manager_obj = in_tftpd.get_manager(None)

    # Act
    manager_obj.write_boot_files()

    # Assert
    assert False


def test_manager_sync_single_system():
    # Arrange
    manager_obj = in_tftpd.get_manager(None)

    # Act
    manager_obj.sync_single_system(None, None)

    # Assert
    assert False


def test_manager_add_single_distro():
    # Arrange
    manager_obj = in_tftpd.get_manager(None)

    # Act
    manager_obj.add_single_distro(None)

    # Assert
    assert False


def test_manager_sync_systems():
    # Arrange
    manager_obj = in_tftpd.get_manager(None)

    # Act
    manager_obj.sync_systems()

    # Assert
    assert False


def test_manager_sync():
    # Arrange
    manager_obj = in_tftpd.get_manager(None)

    # Act
    manager_obj.sync()

    # Assert
    assert False


@pytest.mark.skip("TODO")
@pytest.mark.parametrize(
    "input_systems, input_verbose, expected_output",
    [("t1.example.org", True, "t1.example.org")],
)
def test_sync_systems(input_systems, input_verbose, expected_output):
    # Arrange
    mcollection = Mock()
    manager_obj = in_tftpd.get_manager(mcollection)
    # mock tftpgen

    # Act
    # .sync_systems(input_systems, input_verbose)

    # Assert
    assert False
