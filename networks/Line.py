# Line Class
# May 30 2024

from networks.Element import Element


class Line(Element):
    
    """
    Represents a transmission line in a power system network.

    :param name: The name of the line.
    :type name: str
    :param from_bus_id: The ID of the "from" bus of the line.
    :type from_bus_id: int
    :param to_bus_id: The ID of the "to" bus of the line.
    :type to_bus_id: int
    :param length_km: Length of the line in kilometers.
    :type length_km: float
    :param max_loading_percent: Maximum loading percentage of the line.
    :type max_loading_percent: float
    :param r_ohm_per_km: Resistance of the line per kilometer in ohms.
    :type r_ohm_per_km: float
    :param x_ohm_per_km: Reactance of the line per kilometer in ohms.
    :type x_ohm_per_km: float
    :param c_nf_per_km: Capacitance of the line per kilometer in nanofarads.
    :type c_nf_per_km: float
    :param r0_ohm_per_km: Zero sequence resistance of the line per kilometer in ohms.
    :type r0_ohm_per_km: float
    :param x0_ohm_per_km: Zero sequence reactance of the line per kilometer in ohms.
    :type x0_ohm_per_km: float
    :param c0_nf_per_km: Zero sequence capacitance of the line per kilometer in nanofarads.
    :type c0_nf_per_km: float
    :param norm_amp: Nominal ampacity of the line.
    :type norm_amp: float
    :param max_amp: Maximum ampacity of the line.
    :type max_amp: float
    :param num_parallel: Number of parallel lines.
    :type num_parallel: int
    :param derating_factor: Derating factor of the line.
    :type derating_factor: float
    :param phases: Phases of the line.
    :type phases: str
    :param type: Type of transmission line, "ol" for overhead line, "cs" for cable system
    :type type: str
    """

    _next_id = 1

    def __init__(self, name: str, from_bus_id: int, to_bus_id: int, length_km: float, max_loading_percent: float, r_ohm_per_km: float, x_ohm_per_km: float, c_nf_per_km: float, r0_ohm_per_km: float, x0_ohm_per_km: float, c0_nf_per_km: float, norm_amp: float, max_amp: float, num_parallel: int, derating_factor: float, phases: str, type: str):
        
        """
        Initializes a Line object.

        :param name: The name of the line.
        :type name: str
        :param from_bus_id: The ID of the "from" bus of the line.
        :type from_bus_id: int
        :param to_bus_id: The ID of the "to" bus of the line.
        :type to_bus_id: int
        :param length_km: Length of the line in kilometers.
        :type length_km: float
        :param max_loading_percent: Maximum loading percentage of the line.
        :type max_loading_percent: float
        :param r_ohm_per_km: Resistance of the line per kilometer in ohms.
        :type r_ohm_per_km: float
        :param x_ohm_per_km: Reactance of the line per kilometer in ohms.
        :type x_ohm_per_km: float
        :param c_nf_per_km: Capacitance of the line per kilometer in nanofarads.
        :type c_nf_per_km: float
        :param r0_ohm_per_km: Zero sequence resistance of the line per kilometer in ohms.
        :type r0_ohm_per_km: float
        :param x0_ohm_per_km: Zero sequence reactance of the line per kilometer in ohms.
        :type x0_ohm_per_km: float
        :param c0_nf_per_km: Zero sequence capacitance of the line per kilometer in nanofarads.
        :type c0_nf_per_km: float
        :param norm_amp: Nominal ampacity of the line.
        :type norm_amp: float
        :param max_amp: Maximum ampacity of the line.
        :type max_amp: float
        :param num_parallel: Number of parallel lines.
        :type num_parallel: int
        :param derating_factor: Derating factor of the line.
        :type derating_factor: float
        :param phases: Phases of the line.
        :type phases: str
        :param type: Type of transmission line, "ol" for overhead line, "cs" for cable system
        :type type: str
        """
        
        super().__init__(name)
        self.__id = Line._next_id
        self.__from_bus_id = from_bus_id
        self.__to_bus_id = to_bus_id
        self.__length_km = length_km
        self.__max_loading_percent = max_loading_percent
        self.__r_ohm_per_km = r_ohm_per_km
        self.__x_ohm_per_km = x_ohm_per_km
        self.__c_nf_per_km = c_nf_per_km
        self.__r0_ohm_per_km = r0_ohm_per_km
        self.__x0_ohm_per_km = x0_ohm_per_km
        self.__c0_nf_per_km = c0_nf_per_km
        self.__norm_amp = norm_amp
        self.__max_amp = max_amp
        self.__num_parallel = num_parallel
        self.__derating_factor = derating_factor
        self.__phases = phases
        self.__type = type
        
        Line._next_id += 1

    def get_property(self, var: str):
        
        """
        Get a property of the generator.

        :param var: The name of the property to retrieve.
        :type var: str
        :return: The value of the requested property.
        :rtype: str or float or bool
        """
        if var == "name":
            self.get_name()
        elif var == "from_bus_id":
            return self.__from_bus_id
        elif var == "to_bus_id":
            return self.__to_bus_id
        elif var == "length_km":
            return self.__length_km
        elif var == "max_loading_percent":
            return self.__max_loading_percent
        elif var == "r_ohm_per_km":
            return self.__r_ohm_per_km
        elif var == "x_ohm_per_km":
            return self.__x_ohm_per_km
        elif var == "c_nf_per_km":
            return self.__c_nf_per_km
        elif var == "r0_ohm_per_km":
            return self.__r0_ohm_per_km
        elif var == "x0_ohm_per_km":
            return self.__x0_ohm_per_km
        elif var == "c0_nf_per_km":
            return self.__c0_nf_per_km
        elif var == "norm_amp":
            return self.__norm_amp
        elif var == "max_amp":
            return self.__max_amp
        elif var == "num_parallel":
            return self.__num_parallel
        elif var == "derating_factor":
            return self.__derating_factor
        elif var == "phases":
            return self.__phases
        elif var == "id":
            return self.__id
        elif var == "type":
            return self.__type
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
        elif var == "length_km":
            self.__length_km = new
        elif var == "max_loading_percent":
            self.__max_loading_percent = new
        elif var == "r_ohm_per_km":
            self.__r_ohm_per_km = new
        elif var == "x_ohm_per_km":
            self.__x_ohm_per_km = new
        elif var == "c_nf_per_km":
            self.__c_nf_per_km = new
        elif var == "r0_ohm_per_km":
            self.__r0_ohm_per_km = new
        elif var == "x0_ohm_per_km":
            self.__x0_ohm_per_km = new
        elif var == "c0_nf_per_km":
            self.__c0_nf_per_km = new
        elif var == "norm_amp":
            self.__norm_amp = new
        elif var == "max_amp":
            self.__max_amp = new
        elif var == "num_parallel":
            self.__num_parallel = new
        elif var == "derating_factor":
            self.__derating_factor = new
        elif var == "phases":
            self.__phases = new
        elif var == "type":
            self.__type = new
        else:
            return "Not a valid variable for this element"
        
    def to_dict(self):
        """
        Convert line attributes to a dictionary.

        :return: Dictionary representation of the object.
        :rtype: dict
        """
        return {
            "name": self.get_name(),
            "id": self.__id,
            "from_bus_id": self.__from_bus_id,
            "to_bus_id": self.__to_bus_id,
            "length_km": self.__length_km,
            "max_loading_percent": self.__max_loading_percent,
            "r_ohm_per_km": self.__r_ohm_per_km,
            "x_ohm_per_km": self.__x_ohm_per_km,
            "c_nf_per_km": self.__c_nf_per_km,
            "r0_ohm_per_km": self.__r0_ohm_per_km,
            "x0_ohm_per_km": self.__x0_ohm_per_km,
            "c0_nf_per_km": self.__c0_nf_per_km,
            "norm_amp": self.__norm_amp,
            "max_amp": self.__max_amp,
            "num_parallel": self.__num_parallel,
            "derating_factor": self.__derating_factor,
            "phases": self.__phases,
            "type": self.__type
        }