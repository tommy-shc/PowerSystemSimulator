from networks.Element import Element

class Bus(Element):
    """
    A class representing a bus in a power system network.

    :param name: The name of the bus.
    :type name: str
    :param vn_kv: The voltage magnitude of the bus in kV.
    :type vn_kv: float
    :param type: The type of the bus.
    :type type: str
    :param zone: The zone to which the bus belongs.
    :type zone: str
    :param max_vm_pu: The maximum voltage magnitude of the bus in per unit.
    :type max_vm_pu: float
    :param min_vm_pu: The minimum voltage magnitude of the bus in per unit.
    :type min_vm_pu: float
    :param in_service: Whether the bus is in service or not.
    :type in_service: bool
    """
    _next_id = 1

    def __init__(self, name: str, vn_kv: float, type: str, zone: str, max_vm_pu: float, min_vm_pu: float, in_service: bool):
        """
        Initializes a Bus object.

        :param name: The name of the bus.
        :type name: str
        :param vn_kv: The voltage magnitude of the bus in kV.
        :type vn_kv: float
        :param type: The type of the bus.
        :type type: str
        :param zone: The zone to which the bus belongs.
        :type zone: str
        :param max_vm_pu: The maximum voltage magnitude of the bus in per unit.
        :type max_vm_pu: float
        :param min_vm_pu: The minimum voltage magnitude of the bus in per unit.
        :type min_vm_pu: float
        :param in_service: Whether the bus is in service or not.
        :type in_service: bool
        """
        super().__init__(name)
        self.__id = Bus._next_id
        self.__vn_kv = vn_kv
        self.__type = type
        self.__zone = zone
        self.__max_vm_pu = max_vm_pu
        self.__min_vm_pu = min_vm_pu
        self.__in_service = in_service

        Bus._next_id += 1

    def get_property(self, var: str):
        """
        Get a property of the bus.

        :param var: The name of the property to retrieve.
        :type var: str
        :return: The value of the requested property.
        :rtype: str or float or bool
        """
        if var == "name":
            return self.get_name()
        elif var == "vn_kv":
            return self.__vn_kv
        elif var == "type":
            return self.__type
        elif var == "zone":
            return self.__zone
        elif var == "max_vm_pu":
            return self.__max_vm_pu
        elif var == "min_vm_pu":
            return self.__min_vm_pu
        elif var == "in_service":
            return self.__in_service
        elif var == "id":
            return self.__id
        else:
            return "Not a valid variable for this element"

    def set_property(self, var: str, new):
        """
        Set a property of the bus.

        :param var: The name of the property to set.
        :type var: str
        :param new: The new value for the property.
        :type new: str or float or bool
        :return: A message indicating the success or failure of the operation.
        :rtype: str
        """
        if var == "name":
            self.set_name(new)
        elif var == "vn_kv":
            self.__vn_kv = new
        elif var == "type":
            self.__type = new
        elif var == "zone":
            self.__zone = new
        elif var == "max_vm_pu":
            self.__max_vm_pu = new
        elif var == "min_vm_pu":
            self.__min_vm_pu = new
        elif var == "in_service":
            self.__in_service = new
        else:
            return "Not a valid variable for this element"
        
    def to_dict(self):
        """
        Convert bus attributes to a dictionary.

        :return: Dictionary representation of the object.
        :rtype: dict
        """
        return {
            "name": self.get_name(),
            "id": self.__id,
            "vn_kv": self.__vn_kv,
            "type": self.__type,
            "zone": self.__zone,
            "max_vm_pu": self.__max_vm_pu,
            "min_vm_pu": self.__min_vm_pu,
            "in_service": self.__in_service
        }
