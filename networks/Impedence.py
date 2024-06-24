#Impedence Class
#May 30, 2024

from networks.Element import Element

class Impedence(Element):
    
    """
    A class representing an impedance element in a power system network.

    :param name: The name of the impedance element.
    :type name: str
    :param from_bus_id: The ID of the "from" bus of the impedance element.
    :type from_bus_id: int
    :param to_bus_id: The ID of the "to" bus of the impedance element.
    :type to_bus_id: int
    :param r_pu: The per unit resistance of the impedance.
    :type r_pu: float
    :param x_pu: The per unit reactance of the impedance.
    :type x_pu: float
    :param kv: The voltage magnitude associated with the impedance in kilovolts (kV).
    :type kv: float
    :param kvar: The apparent power rating of the impedance in kilovolt-amperes reactive (kVAR).
    :type kvar: float
    """

    _next_id = 1

    def __init__(self,name: str,from_bus_id: int, to_bus_id: int, r_pu: float,x_pu: float,kv: float, kvar: float):
        
        """
        Initializes an Impedence object.

        :param name: The name of the impedance element.
        :type name: str
        :param from_bus_id: The ID of the "from" bus of the impedance element.
        :type from_bus_id: int
        :param to_bus_id: The ID of the "to" bus of the impedance element.
        :type to_bus_id: int
        :param r_pu: The per unit resistance of the impedance.
        :type r_pu: float
        :param x_pu: The per unit reactance of the impedance.
        :type x_pu: float
        :param kv: The voltage magnitude associated with the impedance in kilovolts (kV).
        :type kv: float
        :param kvar: The apparent power rating of the impedance in kilovolt-amperes reactive (kVAR).
        :type kvar: float
        """

        super().__init__(name)
        self.__id = Impedence._next_id
        self.__from_bus_id = from_bus_id
        self.__to_bus_id = to_bus_id
        self.__r_pu = r_pu
        self.__x_pu = x_pu
        self.__kv = kv
        self.__kvar = kvar
        
        Impedence._next_id += 1

    def get_property(self, var: str):
        
        """
        Get a property of the generator.

        :param var: The name of the property to retrieve.
        :type var: str
        :return: The value of the requested property.
        :rtype: str or float or bool
        """
        if var == "name":
            return self.get_name()
        elif var == "from_bus_id":
            return self.__from_bus_id
        elif var == "to_bus_id":
            return self.__to_bus_id
        elif var == "r_pu":
            return self.__r_pu
        elif var == "x_pu":
            return self.__x_pu
        elif var == "kv":
            return self.__kv
        elif var == "kvar":
            return self.__kvar
        elif var == "id":
            return self.__id
        else:
            return "Not a valid variable for this element"
        
    def set_property(self, var: str, new):
        
        """
        Set a property of the generator.

        :param var: The name of the property to set.
        :type var: str
        :param new: The new value for the property.
        :type new: str or float or bool
        :return: A message indicating the success or failure of the operation.
        :rtype: str
        """
        if var == "name":
            self.set_name(new)
        elif var == "from_bus_id":
            self.__from_bus_id = new
        elif var == "to_bus_id":
            self.__to_bus_id = new
        elif var == "r_pu":
            self.__r_pu = new
        elif var == "x_pu":
            self.__x_pu = new
        elif var == "kv":
            self.__kv = new
        elif var == "kvar":
            self.__kvar = new
        else:
            return "Not a valid variable for this element"
        
    def to_dict(self):
        """
        Convert impdence attributes to a dictionary.

        :return: Dictionary representation of the object.
        :rtype: dict
        """
        return {
            "name": self.get_name(),
            "id": self.__id,
            "from_bus_id": self.__from_bus_id,
            "to_bus_id": self.__to_bus_id,
            "r_pu": self.__r_pu,
            "x_pu": self.__x_pu,
            "kv": self.__kv,
            "kvar": self.__kvar
        }

        