from cobbler.modules.installation import post_report


def test_register():
    # Arrange & Act
    result = post_report.register()

    # Assert
    assert result == "/var/lib/cobbler/triggers/install/post/*"


def test_run():
    # Arrange
    args = None

    # Act
    result = post_report.run(None, args)

    # Assert
    assert result
