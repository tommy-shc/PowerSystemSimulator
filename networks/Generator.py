# Generator Class
# May 30, 2024

from networks.Element import Element


class Generator(Element):
    
    """
    A class representing a generator in a power system network.

    :param name: The name of the generator.
    :type name: str
    :param bus_id: The ID of the bus to which the generator is connected.
    :type bus_id: int
    :param p_kw: Active power output of the generator in kilowatts (kW).
    :type p_kw: float
    :param q_kvar: Reactive power output of the generator in kilovolt-amperes reactive (kVAR).
    :type q_kvar: float
    :param kv: Voltage magnitude of the generator in kilovolts (kV).
    :type kv: float
    :param kva: Apparent power rating of the generator in kilovolt-amperes (kVA).
    :type kva: float
    :param pvfactor: Power factor of the generator.
    :type pvfactor: float
    :param fixed: Whether the generator is fixed or not.
    :type fixed: bool
    :param max_p_kw: Maximum active power output of the generator in kilowatts (kW).
    :type max_p_kw: float
    :param min_p_kw: Minimum active power output of the generator in kilowatts (kW).
    :type min_p_kw: float
    :param max_q_kvar: Maximum reactive power output of the generator in kilovolt-amperes reactive (kVAR).
    :type max_q_kvar: float
    :param min_q_kvar: Minimum reactive power output of the generator in kilovolt-amperes reactive (kVAR).
    :type min_q_kvar: float
    :param phases: Phases of the generator.
    :type phases: str
    :param subtrans_react_pu: Subtransient reactance of the generator in per unit.
    :type subtrans_react_pu: float
    """

    _next_id = 1

    def __init__(self, name: str, bus_id: int, p_kw: float, q_kvar: float, kv: float, kva: float, pvfactor: float, fixed: bool, max_p_kw: float, min_p_kw: float, max_q_kvar: float, min_q_kvar: float, phases: str, subtrans_react_pu: float):
        
        """
        Initializes a Generator object.

        :param name: The name of the generator.
        :type name: str
        :param bus_id: The ID of the bus to which the generator is connected.
        :type bus_id: int
        :param p_kw: Active power output of the generator in kilowatts (kW).
        :type p_kw: float
        :param q_kvar: Reactive power output of the generator in kilovolt-amperes reactive (kVAR).
        :type q_kvar: float
        :param kv: Voltage magnitude of the generator in kilovolts (kV).
        :type kv: float
        :param kva: Apparent power rating of the generator in kilovolt-amperes (kVA).
        :type kva: float
        :param pvfactor: Power factor of the generator.
        :type pvfactor: float
        :param fixed: Whether the generator is fixed or not.
        :type fixed: bool
        :param max_p_kw: Maximum active power output of the generator in kilowatts (kW).
        :type max_p_kw: float
        :param min_p_kw: Minimum active power output of the generator in kilowatts (kW).
        :type min_p_kw: float
        :param max_q_kvar: Maximum reactive power output of the generator in kilovolt-amperes reactive (kVAR).
        :type max_q_kvar: float
        :param min_q_kvar: Minimum reactive power output of the generator in kilovolt-amperes reactive (kVAR).
        :type min_q_kvar: float
        :param phases: Phases of the generator.
        :type phases: str
        :param subtrans_react_pu: Subtransient reactance of the generator in per unit.
        :type subtrans_react_pu: float
        """
        
        super().__init__(name)
        self.__id = Generator._next_id
        self.__bus_id = bus_id
        self.__p_kw = p_kw
        self.__q_kvar = q_kvar
        self.__kv = kv
        self.__kva = kva
        self.__pvfactor = pvfactor
        self.__fixed = fixed
        self.__max_p_kw = max_p_kw
        self.__min_p_kw = min_p_kw
        self.__max_q_kvar = max_q_kvar
        self.__min_q_kvar = min_q_kvar
        self.__phases = phases
        self.__subtrans_react_pu = subtrans_react_pu

        Generator._next_id += 1


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
        elif var == "pvfactor":
            return self.__pvfactor
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
        elif var == "pvfactor":
            self.__pvfactor = new
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
        Convert generator attributes to a dictionary.

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
            "pvfactor": self.__pvfactor,
            "fixed": self.__fixed,
            "max_p_kw": self.__max_p_kw,
            "min_p_kw": self.__min_p_kw,
            "max_q_kvar": self.__max_q_kvar,
            "min_q_kvar": self.__min_q_kvar,
            "phases": self.__phases,
            "subtrans_react_pu": self.__subtrans_react_pu   
        }

