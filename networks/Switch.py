#Switch Class
#May 30, 2024

from networks.Element import Element

class Switch(Element):

    #Add Element_id (int) variable, the id of the element the switch is attached to
    #index of the element: bus id if et == “b”, line id if et == “l”, trafo id if et == “t” <- PP Documentation

    """
    Represents a switch element in a power system network.

    :param bus_id: The ID of the bus where the switch is connected.
    :type bus_id: int
    :param name: The name of the switch.
    :type name: str
    :param type: The type of the switch.
    :type type: str
    :param closed: Whether the switch is closed or not.
    :type closed: bool
    :param base_freq: The base frequency of the switch.
    :type base_freq: float
    :param max_ka: Maximum kiloampere rating of the switch.
    :type max_ka: float
    """

    _next_id = 1

    def __init__(self, name: str, bus_id: int, type: str, closed: bool, base_freq: float, max_ka: float):
        
        """
        Initializes a Switch object.

        :param bus_id: The ID of the bus where the switch is connected.
        :type bus_id: int
        :param name: The name of the switch.
        :type name: str
        :param type: The type of the switch.
        :type type: str
        :param closed: Whether the switch is closed or not.
        :type closed: bool
        :param base_freq: The base frequency of the switch.
        :type base_freq: float
        :param max_ka: Maximum kiloampere rating of the switch.
        :type max_ka: float
        """
        
        super().__init__(name)
        self.__id = Switch._next_id
        self.__bus_id = bus_id
        self.__type = type
        self.__closed = closed 
        self.__base_freq = base_freq
        self.__max_ka = max_ka
        
        Switch._next_id += 1

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
        elif var == "bus_id":
            return self.__bus_id
        elif var == "type":
            return self.__type
        elif var == "closed":
            return self.__closed
        elif var == "base_freq":
            return self.__base_freq
        elif var == "max_ka":
            return self.__max_ka
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
        elif var == "bus_id":
            self.__bus_id = new
        elif var == "type":
            self.__type = new
        elif var == "closed":
            self.__closed = new
        elif var == "base_freq":
            self.__base_freq = new
        elif var == "max_ka":
            self.__max_ka = new
        else:
            return "Not a valid variable for this element"
        
    def to_dict(self):
        """
        Convert switch attributes to a dictionary.

        :return: Dictionary representation of the object.
        :rtype: dict
        """
        return {
            "name": self.get_name(),
            "id": self.__id,
            "bus_id": self.__bus_id,
            "type": self.__type,
            "closed": self.__closed,
            "base_freq": self.__base_freq,
            "max_ka": self.__max_ka
        }
