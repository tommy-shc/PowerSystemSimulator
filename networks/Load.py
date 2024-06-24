# Load Class
# May 30, 2024

from networks.Element import Element


class Load(Element):
    
    """
    Represents a load element in a power system network.

    :param name: The name of the load.
    :type name: str
    :param bus_id: The ID of the bus where the load is connected.
    :type bus_id: int
    :param p_kw: Active power of the load in kilowatts (kW).
    :type p_kw: float
    :param q_kvar: Reactive power of the load in kilovolt-amperes reactive (kVAR).
    :type q_kvar: float
    :param kv: Voltage magnitude associated with the load in kilovolts (kV).
    :type kv: float
    :param kva: Apparent power rating of the load in kilovolt-amperes (kVA).
    :type kva: float
    :param const_z_percent: Constant impedance percentage.
    :type const_z_percent: float
    :param const_i_percent: Constant current percentage.
    :type const_i_percent: float
    :param fixed: Whether the load is fixed or not.
    :type fixed: bool
    :param max_p_kw: Maximum active power of the load in kilowatts (kW).
    :type max_p_kw: float
    :param min_p_kw: Minimum active power of the load in kilowatts (kW).
    :type min_p_kw: float
    :param max_q_kvar: Maximum reactive power of the load in kilovolt-amperes reactive (kVAR).
    :type max_q_kvar: float
    :param min_q_kvar: Minimum reactive power of the load in kilovolt-amperes reactive (kVAR).
    :type min_q_kvar: float
    """

    _next_id = 1

    def __init__(self, name: str, bus_id: int, p_kw: float, q_kvar: float, kv: float, kva: float, const_z_percent: float, const_i_percent: float, fixed: bool, max_p_kw: float, min_p_kw: float, max_q_kvar: float, min_q_kvar: float):
        
        """
        Initializes a Load object.

        :param name: The name of the load.
        :type name: str
        :param bus_id: The ID of the bus where the load is connected.
        :type bus_id: int
        :param p_kw: Active power of the load in kilowatts (kW).
        :type p_kw: float
        :param q_kvar: Reactive power of the load in kilovolt-amperes reactive (kVAR).
        :type q_kvar: float
        :param kv: Voltage magnitude associated with the load in kilovolts (kV).
        :type kv: float
        :param kva: Apparent power rating of the load in kilovolt-amperes (kVA).
        :type kva: float
        :param const_z_percent: Constant impedance percentage.
        :type const_z_percent: float
        :param const_i_percent: Constant current percentage.
        :type const_i_percent: float
        :param fixed: Whether the load is fixed or not.
        :type fixed: bool
        :param max_p_kw: Maximum active power of the load in kilowatts (kW).
        :type max_p_kw: float
        :param min_p_kw: Minimum active power of the load in kilowatts (kW).
        :type min_p_kw: float
        :param max_q_kvar: Maximum reactive power of the load in kilovolt-amperes reactive (kVAR).
        :type max_q_kvar: float
        :param min_q_kvar: Minimum reactive power of the load in kilovolt-amperes reactive (kVAR).
        :type min_q_kvar: float
        """
        
        super().__init__(name)
        self.__id = Load._next_id
        self.__bus_id = bus_id
        self.__p_kw = p_kw
        self.__q_kvar = q_kvar
        self.__kv = kv
        self.__kva = kva
        self.__const_z_percent = const_z_percent
        self.__const_i_percent = const_i_percent
        self.__fixed = fixed
        self.__max_p_kw = max_p_kw
        self.__min_p_kw = min_p_kw
        self.__max_q_kvar = max_q_kvar
        self.__min_q_kvar = min_q_kvar
        
        Load._next_id += 1

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
        elif var == "q_kvar":
            return self.__q_kvar
        elif var == "kv":
            return self.__kv
        elif var == "kva":
            return self.__kva
        elif var == "const_z_percent":
            return self.__const_z_percent
        elif var == "const_i_percent":
            return self.__const_i_percent
        elif var == "fixed":
            return self.__fixed
        elif var == "max_p_kw":
            return self.__max_p_kw
        elif var == "min_p_kw":
            return self.__min_p_kw
        elif var == "max_q_kvar":
            return self.__max_q_kvar
        elif var == "min_q_kvar":
            return self.__min_q_kvar
        elif var == "phases":
            return self.__phases
        elif var == "subtrans_react_pu":
            return self.__subtrans_react_pu
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
        elif var == "q_kvar":
            self.__q_kvar = new
        elif var == "kv":
            self.__kv = new
        elif var == "kva":
            self.__kva = new
        elif var == "const_z_percent":
            self.__const_z_percent = new
        elif var == "const_i_percent":
            self.__const_i_percent = new
        elif var == "fixed":
            self.__fixed = new
        elif var == "max_p_kw":
            self.__max_p_kw = new
        elif var == "min_p_kw":
            self.__min_p_kw = new
        elif var == "max_q_kvar":
            self.__max_q_kvar = new
        elif var == "min_q_kvar":
            self.__min_q_kvar = new
        elif var == "phases":
            self.__phases = new
        elif var == "subtrans_react_pu":
            self.__subtrans_react_pu = new
        else:
            return "Not a valid variable for this element"
    
    def to_dict(self):
        """
        Convert load attributes to a dictionary.

        :return: Dictionary representation of the object.
        :rtype: dict
        """
        return {
            "name": self.get_name(),
            "id": self.__id,
            "bus_id": self.__bus_id,
            "p_kw": self.__p_kw,
            "q_kvar": self.__q_kvar,
            "kv": self.__kv,
            "kva": self.__kva,
            "const_z_percent": self.__const_z_percent,
            "const_i_percent": self.__const_i_percent,
            "fixed": self.__fixed,
            "max_p_kw": self.__max_p_kw,
            "min_p_kw": self.__min_p_kw,
            "max_q_kvar": self.__max_q_kvar,
            "min_q_kvar": self.__min_q_kvar
        }
       