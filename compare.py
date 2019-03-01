import xml.etree.cElementTree as ET
import inspect
import os
import rsd_lib.compare.mapping as mapping
import rsd_lib


def compare():
    method_prifx = 'rsd_lib.resources.v2_1.'
    for filename in os.listdir('./xml'):
        if filename in mapping.dic.keys():
            print("#################")
            print(filename)
            tree = ET.parse('./xml/' + filename)
            root = tree.getroot()
            # property set
            prop_set = set()
            # navigation property set
            navigation_set = set()
            # all set
            sum_set = set()
            # class set
            class_set = set()
            # method set to check whether decorator is right
            method_set = set()
            # mapping from method without underline to underline
            method_dict = {}
            # int and bool type dict
            adapter = {}
            for child in tree.iter(
                    tag='{http://docs.oasis-open.org/odata/ns/edmx}Reference'):
                if child.attrib['Uri'] == 'Resource.xml':
                    resource_list = ['identity', 'description', 'name', 'uuid',
                                     'links', 'oem', 'state',
                                     'health', 'status']
                    resource_set = set()
                    for item in resource_list:
                        resource_set.add(item)
                    sum_set = resource_set
            for elem in tree.iter(
                    tag='{http://docs.oasis-open.org/odata/ns/edm}Property'):
                # print(elem.attrib['Name'].lower(), ',', elem.attrib['Type'])
                prop_set.add(elem.attrib['Name'].lower())
                if elem.attrib['Type'] in (
                        'Edm.Boolean', 'Edm.Int32', 'Edm.Int64'):
                    adapter[elem.attrib['Name'].lower()] = elem.attrib['Type']

            # navigation set
            for elem in tree.iter(
                    tag='{http://docs.oasis-open.org/odata/ns/edm}NavigationProperty'):
                # print(elem.attrib['Name'].lower(), ',', elem.attrib['Type'])
                navigation_set.add(elem.attrib['Name'].lower())

            sum_set = (sum_set | prop_set | navigation_set)

            # traverse the class and add attr in class_set
            for name, obj in inspect.getmembers(mapping.dic[filename][0]):
                if inspect.isclass(obj):
                    # print(obj)
                    # print(obj.__dict__)
                    for attr in dir(obj):
                        if not callable(attr) and not attr.startswith(
                                "__") and not attr.startswith(
                            "_abc") and not attr.startswith(
                            "_do") and not attr.startswith("_par") \
                                and not attr.startswith(
                            "_load"):
                            # print(attr)
                            class_set.add(attr.replace('_', ''))
                            method_dict[attr.replace('_', '')] = attr

            print('Property Miss:', prop_set - class_set)
            print('NavigationProperty Miss:', navigation_set - class_set)
            method_set = navigation_set & class_set

            # to check whether decorator is right
            for item in method_set:
                if mapping.dic[filename][1]:
                    if method_dict[item] in dir(
                            eval(method_prifx + mapping.dic[filename][1])):
                        obj = method_prifx + mapping.dic[filename][1] + "." + \
                              method_dict[item]
                        if not isinstance(eval(obj), property):
                            print('wrong decorator:', method_dict[item])

            # format class set to get redundant
            list = ['get', 'invalidate', 'keys', 'values', 'items', 'json',
                    'refresh', 'redfishversion', 'getmembers', 'getmember',
                    'path', 'update', 'delete', 'membersidentities',
                    'resourcetype', 'healthrollup','racksupportsdisaggregatedpowercooling','parentid','geotag','rmmpresent']
            for item in list:
                if item in class_set:
                    class_set.remove(item)
            temp = set()
            for item in class_set:
                if item.endswith('collectionpath'):
                    item = item.replace('collectionpath', 's').replace('get',
                                                                       '')
                    temp.add(item)
                else:
                    if item.startswith('get') and item.endswith('path'):
                        item = item.replace('get', '').replace('path', '')
                    temp.add(item)

            print('Redundant:', temp - sum_set)
            print('type check:', adapter)


def parse_resource(filename):
    tree = ET.parse('./xml/' + filename)
    root = tree.getroot()
    for child in root:
        print("############################")
        print('child-tag是：', child.tag, ',child.attrib：', child.attrib,
              ',child.text：', child.text)
        for sub1 in child:
            print('sub1-tag是：', sub1.tag, ',sub1.attrib：', sub1.attrib,
                  ',sub1.text：', sub1.text)
            for sub2 in sub1:
                print('sub2-tag是：', sub2.tag, ',sub2.attrib：', sub2.attrib,
                      ',sub2.text：', sub2.text)


compare()
# parse_resource('RedfishExtensions.xml')
