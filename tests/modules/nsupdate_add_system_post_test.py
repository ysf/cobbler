from unittest.mock import MagicMock

from cobbler.api import CobblerAPI
from cobbler.modules import nsupdate_add_system_post


def test_register():
    # Arrange & Act
    result = nsupdate_add_system_post.register()

    # Assert
    assert result == "/var/lib/cobbler/triggers/add/system/post/*"


def test_run():
    # Arrange
    api = MagicMock(spec=CobblerAPI)
    args = ["testname"]

    # Act
    result = nsupdate_add_system_post.run(api, args)

    # Assert
    assert result
