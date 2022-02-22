from cobbler import autoinstall_manager

# 2022-02-28_093028_validate_autoinstall_files] 2022-02-28T09:30:29 - DEBUG | running python triggers from /var/lib/cobbler/triggers/task/validate_autoinstall_files/pre/*
# [2022-02-28_093028_validate_autoinstall_files] 2022-02-28T09:30:29 - DEBUG | running shell triggers from /var/lib/cobbler/triggers/task/validate_autoinstall_files/pre/*
# [2022-02-28_093028_validate_autoinstall_files] 2022-02-28T09:30:29 - DEBUG | shell triggers finished successfully
# [2022-02-28_093028_validate_autoinstall_files] 2022-02-28T09:30:29 - INFO | validate_autoinstall_files
# [2022-02-28_093028_validate_autoinstall_files] 2022-02-28T09:30:29 - INFO | ----------------------------
# [2022-02-28_093028_validate_autoinstall_files] 2022-02-28T09:30:29 - DEBUG | osversion:
# [2022-02-28_093028_validate_autoinstall_files] 2022-02-28T09:30:29 - INFO | Exception occurred: <class 'TypeError'>
# [2022-02-28_093028_validate_autoinstall_files] 2022-02-28T09:30:29 - INFO | Exception value: unhashable type: 'Profile'
# [2022-02-28_093028_validate_autoinstall_files] 2022-02-28T09:30:29 - INFO | Exception Info:
#   File "/usr/lib/python3.6/site-packages/cobbler/remote.py", line 99, in run
#     rc = self._run(self)
#
#   File "/usr/lib/python3.6/site-packages/cobbler/remote.py", line 260, in runner
#     return self.remote.api.validate_autoinstall_files()
#
#   File "/usr/lib/python3.6/site-packages/cobbler/api.py", line 1372, in validate_autoinstall_files
#     autoinstall_mgr.validate_autoinstall_files()
#
#   File "/usr/lib/python3.6/site-packages/cobbler/autoinstall_manager.py", line 329, in validate_autoinstall_files
#     (success, errors_type, errors) = self.validate_autoinstall_file(x, True)
#
#   File "/usr/lib/python3.6/site-packages/cobbler/autoinstall_manager.py", line 309, in validate_autoinstall_file
#     self.generate_autoinstall(profile=obj)
#
#   File "/usr/lib/python3.6/site-packages/cobbler/autoinstall_manager.py", line 268, in generate_autoinstall
#     return self.autoinstallgen.generate_autoinstall_for_profile(profile)
#
#   File "/usr/lib/python3.6/site-packages/cobbler/autoinstallgen.py", line 347, in generate_autoinstall_for_profile
#     g = self.api.find_profile(name=g)
#
#   File "/usr/lib/python3.6/site-packages/cobbler/api.py", line 931, in find_profile
#     return self._collection_mgr.profiles().find(name=name, return_list=return_list, no_errors=no_errors, **kargs)
#
#   File "/usr/lib/python3.6/site-packages/cobbler/cobbler_collections/collection.py", line 127, in find
#     return self.listing.get(kargs["name"], None)
#
# [2022-02-28_093028_validate_autoinstall_files] 2022-02-28T09:30:29 - ERROR | ### TASK FAILED ###


def test_create_autoinstallation_manager():
    # Arrange
    # TODO

    # Act
    result = autoinstall_manager.AutoInstallationManager(None)

    # Assert
    isinstance(result, autoinstall_manager.AutoInstallationManager)
