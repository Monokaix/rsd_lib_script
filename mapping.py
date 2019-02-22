from rsd_lib.resources.v2_1.chassis import *
from rsd_lib.resources.v2_1.ethernet_switch import *
from rsd_lib.resources.v2_1.event_service import *
from rsd_lib.resources.v2_1.fabric import *
from rsd_lib.resources.v2_1.manager import *
from rsd_lib.resources.v2_1.storage_service import *
from rsd_lib.resources.v2_1.system import *
from rsd_lib.resources.v2_1.task import *

# mapping from xml to class
dic = dict([
    ('Chassis.xml', [chassis, 'chassis.Chassis']),
    # ('PCIeDevice.xml', [pcie_device, None]),
    # ('PCIeFunction.xml', [pcie_function, None]),
    #
    # ('Power.xml', [power, None]),
    # ('PowerZone.xml', [power_zone, None]),
    # ('Thermal.xml', [thermal, None]),
    # ('ThermalZone.xml', [thermal_zone, None]),
    # ('EthernetSwitchACL.xml', [acl, None]),
    # ('EthernetSwitchACLRule.xml', [acl_rule, None]),
    # (
    #     'EthernetSwitch.xml',
    #     [ethernet_switch, 'ethernet_switch.EthernetSwitch']),
    # ('EthernetSwitchPort.xml', [port, None]),
    #
    # ('EthernetSwitchStaticMAC.xml', [static_mac, None]),
    # ('EventService.xml', [event_service, 'event_service.EventService']),
    #
    # ('Fabric.xml', [fabric, 'fabric.Fabric']),
    # ('Port.xml', [port, None]),
    # ('Switch.xml', [switch, None]),
    # ('Zone.xml', [zone, None]),
    # ('Manager.xml', [manager, 'manager.Manager']),
    # ('LogicalDrive.xml', [logical_drive, None]),
    # ('PhysicalDrive.xml', [physical_drive, None]),
    # ('RemoteTarget.xml', [remote_target, None]),
    # (
    #     'StorageService.xml',
    #     [storage_service, 'storage_service.StorageService']),
    #
    # ('EthernetInterface.xml',
    #  [ethernet_interface, None]),
    # ('Memory.xml', [memory, None]),
    # ('NetworkDeviceFunction.xml', [network_device_function,
    #                                None]),
    # ('NetworkInterface.xml',
    #  [network_interface, None]),
    # ('Task.xml', [task, 'task.Task']),
    # ('TaskService.xml', [task_service, None]),

])
