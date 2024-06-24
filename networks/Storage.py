#Storage Class
#May 30, 2024

from networks.Element import Element

class Storage(Element):
    
    """
    Represents a storage element in a power system network.

    :param bus_id: The ID of the bus where the storage element is connected.
    :type bus_id: int
    :param name: The name of the storage element.
    :type name: str
    :param p_kw: Active power of the storage element in kilowatts (kW).
    :type p_kw: float
    :param p_kvar: Reactive power of the storage element in kilovolt-amperes reactive (kVAR).
    :type p_kvar: float
    :param max_e_kwh: Maximum energy capacity of the storage element in kilowatt-hours (kWh).
    :type max_e_kwh: float
    :param min_e_kwh: Minimum energy capacity of the storage element in kilowatt-hours (kWh).
    :type min_e_kwh: float
    :param soc_percent: State of charge (SOC) percentage of the storage element.
    :type soc_percent: float
    :param max_p_mv: Maximum power charging/discharging rate of the storage element in megavolt-amperes (MV).
    :type max_p_mv: float
    :param min_p_kw: Minimum active power of the storage element in kilowatts (kW).
    :type min_p_kw: float
    :param max_q_mvar: Maximum reactive power of the storage element in megavolt-amperes reactive (MVAr).
    :type max_q_mvar: float
    :param min_q_kvar: Minimum reactive power of the storage element in kilovolt-amperes reactive (kVAR).
    :type min_q_kvar: float
    """

    _next_id = 1

    def __init__(self, name: str, bus_id: int, p_kw: float, p_kvar: float, max_e_kwh: float, min_e_kwh: float, soc_percent: float, max_p_mv: float, min_p_kw: float, max_q_mvar: float, min_q_kvar: float):
        
        """
        Initializes a Storage object.

        :param bus_id: The ID of the bus where the storage element is connected.
        :type bus_id: int
        :param name: The name of the storage element.
        :type name: str
        :param p_kw: Active power of the storage element in kilowatts (kW).
        :type p_kw: float
        :param p_kvar: Reactive power of the storage element in kilovolt-amperes reactive (kVAR).
        :type p_kvar: float
        :param max_e_kwh: Maximum energy capacity of the storage element in kilowatt-hours (kWh).
        :type max_e_kwh: float
        :param min_e_kwh: Minimum energy capacity of the storage element in kilowatt-hours (kWh).
        :type min_e_kwh: float
        :param soc_percent: State of charge (SOC) percentage of the storage element.
        :type soc_percent: float
        :param max_p_mv: Maximum power charging/discharging rate of the storage element in megavolt-amperes (MV).
        :type max_p_mv: float
        :param min_p_kw: Minimum active power of the storage element in kilowatts (kW).
        :type min_p_kw: float
        :param max_q_mvar: Maximum reactive power of the storage element in megavolt-amperes reactive (MVAr).
        :type max_q_mvar: float
        :param min_q_kvar: Minimum reactive power of the storage element in kilovolt-amperes reactive (kVAR).
        :type min_q_kvar: float
        """
        
        super().__init__(name)
        self.__id = Storage._next_id
        self.__bus_id = bus_id
        self.__p_kw = p_kw
        self.__p_kvar = p_kvar 
        self.__max_e_kwh = max_e_kwh
        self.__min_e_kwh = min_e_kwh
        self.__soc_percent = soc_percent
        self.__max_p_mv = max_p_mv
        self.__min_p_kw = min_p_kw
        self.__max_q_mvar = max_q_mvar
        self.__min_q_kvar = min_q_kvar
        
        Storage._next_id += 1

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
        elif var == "p_kw":
            return self.__p_kw
        elif var == "p_kvar":
            return self.__p_kvar
        elif var == "max_e_kwh":
            return self.__max_e_kwh
        elif var == "min_e_kwh":
            return self.__min_e_kwh
        elif var == "soc_percent":
            return self.__soc_percent
        elif var == "max_p_mv":
            return self.__max_p_mv
        elif var == "min_p_kw":
            return self.__min_p_kw
        elif var == "max_q_mvar":
            return self.__max_q_mvar
        elif var == "min_q_kvar":
            return self.__min_q_kvar
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
        elif var == "p_kw":
            self.__p_kw = new
        elif var == "p_kvar":
            self.__p_kvar = new
        elif var == "max_e_kwh":
            self.__max_e_kwh = new
        elif var == "min_e_kwh":
            self.__min_e_kwh = new
        elif var == "soc_percent":
            self.__soc_percent = new
        elif var == "max_p_mv":
            self.__max_p_mv = new
        elif var == "min_p_kw":
            self.__min_p_kw = new
        elif var == "max_q_mvar":
            self.__max_q_mvar = new
        elif var == "min_q_kvar":
            self.__min_q_kvar = new

        else:
            return "Not a valid variable for this element"
        
    def to_dict(self):
        """
        Convert storage attributes to a dictionary.

        :return: Dictionary representation of the object.
        :rtype: dict
        """
        return {
            "name": self.get_name(),
            "id": self.__id,
            "bus_id": self.__bus_id,
            "p_kw": self.__p_kw,
            "p_kvar": self.__p_kvar,
            "max_e_kwh": self.__max_e_kwh,
            "min_e_kwh": self.__min_e_kwh,
            "soc_percent": self.__soc_percent,
            "max_p_mv": self.__max_p_mv,
            "min_p_kw": self.__min_p_kw,
            "max_q_mvar": self.__max_q_mvar,
            "min_q_kvar": self.__min_q_kvar
        }
