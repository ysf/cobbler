from unittest.mock import MagicMock

import pytest

from cobbler.api import CobblerAPI
from cobbler.modules.managers import isc
from cobbler.items.distro import Distro
from cobbler.items.profile import Profile
from cobbler.items.system import System
from cobbler.settings import Settings
from cobbler.cobbler_collections.manager import CollectionManager


@pytest.fixture
def collection_mgr_mock():
    api_mock = MagicMock(spec=CobblerAPI)
    settings_mock = MagicMock(spec=Settings)
    settings_mock.server = "127.0.0.1"
    settings_mock.default_template_type = "cheetah"
    settings_mock.cheetah_import_whitelist = ["re"]
    settings_mock.always_write_dhcp_entries = True
    settings_mock.http_port = 80
    settings_mock.next_server_v4 = ""
    settings_mock.next_server_v6 = ""
    settings_mock.default_ownership = ""
    settings_mock.default_virt_bridge = ""
    settings_mock.default_virt_type = "auto"
    settings_mock.default_virt_ram = 64
    settings_mock.restart_dhcp = True
    settings_mock.enable_ipxe = True
    settings_mock.enable_menu = True
    settings_mock.virt_auto_boot = True
    settings_mock.default_name_servers = []
    settings_mock.default_name_servers_search = []
    settings_mock.manage_dhcp_v4 = True
    settings_mock.manage_dhcp_v6 = True
    settings_mock.jinja2_includedir = ""
    settings_mock.default_virt_disk_driver = "raw"
    api_mock.settings.return_value = settings_mock
    collection_mgr = MagicMock(spec=CollectionManager)
    collection_mgr.api = api_mock
    test_distro = Distro(api_mock)
    test_distro.name = "test"
    collection_mgr.distros.return_value = MagicMock(return_value=[test_distro])
    test_profile = Profile(api_mock)
    test_profile.name = "test"
    collection_mgr.profiles.return_value = MagicMock(return_value=[test_profile])
    test_system = System(api_mock)
    test_system.name = "test"
    collection_mgr.systems.return_value = MagicMock(return_value=[test_system])
    collection_mgr.repos.return_value = MagicMock(return_value=[])
    return collection_mgr


def test_register():
    # Arrange & Act
    result = isc.register()

    # Assert
    assert result == "manage"


def test_get_manager(collection_mgr_mock):
    # Arrange
    isc.MANAGER = None

    # Act
    result = isc.get_manager(collection_mgr_mock)

    # Assert
    isinstance(result, isc._IscManager)


def test_manager_what():
    # Arrange & Act & Assert
    assert isc._IscManager.what() == "isc"


def test_manager_write_v4_config(mocker):
    # Arrange
    isc.MANAGER = None
    manager = isc.get_manager(collection_mgr_mock)
    mocked_templar = mocker.patch.object(manager, "templar", autospec=True)

    # Act
    manager.write_v4_config()

    # Assert
    assert mocked_templar.render.call_count == 1
    mocked_templar.render.assert_called_with("", {}, "/etc/dhcpd.conf")


def test_manager_write_v6_config(mocker):
    # Arrange
    isc.MANAGER = None
    manager = isc.get_manager(collection_mgr_mock)
    mocked_templar = mocker.patch.object(manager, "templar", autospec=True)

    # Act
    manager.write_v6_config()

    # Assert
    assert mocked_templar.render.call_count == 1
    mocked_templar.render.assert_called_with("", {}, "/etc/dhcpd6.conf")


def test_manager_restart_dhcp(mocker, collection_mgr_mock):
    # Arrange
    isc.MANAGER = None
    mocked_subprocess = mocker.patch("cobbler.utils.subprocess_call", autospec=True, return_value=0)
    mocked_service_restart = mocker.patch("cobbler.utils.service_restart", autospec=True, return_value=0)
    manager = isc.get_manager(collection_mgr_mock)

    # Act
    result = manager.restart_dhcp("dhcpd")

    # Assert
    assert mocked_subprocess.call_count == 1
    mocked_subprocess.assert_called_with("dhcpd -t -q", shell=False)
    assert mocked_service_restart.call_count == 1
    mocked_service_restart.assert_called_with("dhcpd")
    assert result == 0


def test_manager_write_configs(mocker, collection_mgr_mock):
    # Arrange
    isc.MANAGER = None
    manager = isc.get_manager(collection_mgr_mock)
    mocked_v4 = mocker.patch.object(manager, "write_v4_config", autospec=True)
    mocked_v6 = mocker.patch.object(manager, "write_v6_config", autospec=True)

    # Act
    manager.write_configs()

    # Assert
    assert mocked_v4.call_count == 1
    assert mocked_v6.call_count == 1


def test_manager_restart_service(mocker, collection_mgr_mock):
    # Arrange
    isc.MANAGER = None
    manager = isc.get_manager(collection_mgr_mock)
    mocked_restart = mocker.patch.object(manager, "restart_dhcp", autospec=True, return_value=0)
    mocked_service_name = mocker.patch("cobbler.utils.dhcp_service_name", autospec=True, return_value="dhcpd")

    # Act
    result = manager.restart_service()

    # Assert
    assert mocked_service_name.call_count == 1
    assert mocked_restart.call_count == 2
    assert result == 0
