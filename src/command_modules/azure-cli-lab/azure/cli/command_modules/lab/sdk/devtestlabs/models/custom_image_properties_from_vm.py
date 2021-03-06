# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class CustomImagePropertiesFromVm(Model):
    """Properties for creating a custom image from a virtual machine.

    :param source_vm_id: The source vm identifier.
    :type source_vm_id: str
    :param windows_os_info: The Windows OS information of the VM.
    :type windows_os_info: :class:`WindowsOsInfo
     <azure.mgmt.devtestlabs.models.WindowsOsInfo>`
    :param linux_os_info: The Linux OS information of the VM.
    :type linux_os_info: :class:`LinuxOsInfo
     <azure.mgmt.devtestlabs.models.LinuxOsInfo>`
    """

    _attribute_map = {
        'source_vm_id': {'key': 'sourceVmId', 'type': 'str'},
        'windows_os_info': {'key': 'windowsOsInfo', 'type': 'WindowsOsInfo'},
        'linux_os_info': {'key': 'linuxOsInfo', 'type': 'LinuxOsInfo'},
    }

    def __init__(self, source_vm_id=None, windows_os_info=None, linux_os_info=None):
        self.source_vm_id = source_vm_id
        self.windows_os_info = windows_os_info
        self.linux_os_info = linux_os_info
