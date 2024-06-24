# Transformer Class
# May 30, 2024

from networks.Element import Element


class Transformer(Element):
    
    """
    Represents a transformer element in a power system network.

    :param name: The name of the transformer.
    :type name: str
    :param hv_bus_id: The ID of the high-voltage (HV) bus where the transformer is connected.
    :type hv_bus_id: int
    :param lv_bus_id: The ID of the low-voltage (LV) bus where the transformer is connected.
    :type lv_bus_id: int
    :param hv_kv: The high-voltage (HV) rating of the transformer in kilovolts (kV).
    :type hv_kv: float
    :param lv_kv: The low-voltage (LV) rating of the transformer in kilovolts (kV).
    :type lv_kv: float
    :param sn_kva: The apparent power rating of the transformer in kilovolt-amperes (kVA).
    :type sn_kva: float
    :param vk_percent: The short-circuit voltage percentage of the transformer.
    :type vk_percent: float
    :param vkr_percent: The short-circuit voltage resistance percentage of the transformer.
    :type vkr_percent: float
    :param pfe_kw: Iron losses in the transformer in kilowatts (kW).
    :type pfe_kw: float
    :param i0_percent: No-load current percentage of the transformer.
    :type i0_percent: float
    :param tap_min: Minimum tap position of the transformer.
    :type tap_min: float
    :param tap_neutral: Neutral tap position of the transformer.
    :type tap_neutral: float
    :param tap_max: Maximum tap position of the transformer.
    :type tap_max: float
    :param tap_step_percent: Tap step percentage of the transformer.
    :type tap_step_percent: float
    :param rh: Resistance at high voltage (HV) side of the transformer.
    :type rh: float
    :param rl: Resistance at low voltage (LV) side of the transformer.
    :type rl: float
    :param x: Reactance of the transformer.
    :type x: float
    """

    _next_id = 1

    def __init__(self, name: str, hv_bus_id: int, lv_bus_id: int, hv_kv: float, lv_kv: float, sn_kva: float, vk_percent: float, vkr_percent: float, pfe_kw: float, i0_percent: float, tap_min: float, tap_neutral: float, tap_max: float, tap_step_percent: float, rh: float, rl: float, x: float):
        
        """
        Initializes a Transformer object.

        :param name: The name of the transformer.
        :type name: str
        :param hv_bus_id: The ID of the high-voltage (HV) bus where the transformer is connected.
        :type hv_bus_id: int
        :param lv_bus_id: The ID of the low-voltage (LV) bus where the transformer is connected.
        :type lv_bus_id: int
        :param hv_kv: The high-voltage (HV) rating of the transformer in kilovolts (kV).
        :type hv_kv: float
        :param lv_kv: The low-voltage (LV) rating of the transformer in kilovolts (kV).
        :type lv_kv: float
        :param sn_kva: The apparent power rating of the transformer in kilovolt-amperes (kVA).
        :type sn_kva: float
        :param vk_percent: The short-circuit voltage percentage of the transformer.
        :type vk_percent: float
        :param vkr_percent: The short-circuit voltage resistance percentage of the transformer.
        :type vkr_percent: float
        :param pfe_kw: Iron losses in the transformer in kilowatts (kW).
        :type pfe_kw: float
        :param i0_percent: No-load current percentage of the transformer.
        :type i0_percent: float
        :param tap_min: Minimum tap position of the transformer.
        :type tap_min: float
        :param tap_neutral: Neutral tap position of the transformer.
        :type tap_neutral: float
        :param tap_max: Maximum tap position of the transformer.
        :type tap_max: float
        :param tap_step_percent: Tap step percentage of the transformer.
        :type tap_step_percent: float
        :param rh: Resistance at high voltage (HV) side of the transformer.
        :type rh: float
        :param rl: Resistance at low voltage (LV) side of the transformer.
        :type rl: float
        :param x: Reactance of the transformer.
        :type x: float
        """
        
        super().__init__(name)
        self.__id = Transformer._next_id
        self.__hv_bus_id = hv_bus_id
        self.__lv_bus_id = lv_bus_id
        self.__hv_kv = hv_kv
        self.__lv_kv = lv_kv
        self.__sn_kva = sn_kva
        self.__vk_percent = vk_percent
        self.__vkr_percent = vkr_percent
        self.__pfe_kw = pfe_kw
        self.__i0_percent = i0_percent
        self.__tap_min = tap_min
        self.__tap_neutral = tap_neutral
        self.__tap_max = tap_max
        self.__tap_step_percent = tap_step_percent
        self.__rh = rh
        self.__rl = rl
        self.__x = x
        
        Transformer._next_id += 1

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
        elif var == "hv_bus_id":
            return self.__hv_bus_id
        elif var == "lv_bus_id":
            return self.__lv_bus
        elif var == "hv_kv":
            return self.__hv_kv
        elif var == "lv_kv":
            return self.__lv_kv
        elif var == "sn_kva":
            return self.__sn_kva
        elif var == "vk_percent":
            return self.__vk_percent
        elif var == "vkr_percent":
            return self.__vkr_percent
        elif var == "pfe_kw":
            return self.__pfe_kw
        elif var == "i0_percent":
            return self.__i0_percent
        elif var == "tap_min":
            return self.__tap_min
        elif var == "tap_neutral":
            return self.__tap_neutral
        elif var == "tap_max":
            return self.__tap_max
        elif var == "tap_step_percent":
            return self.__tap_step_percent
        elif var == "rh":
            return self.__rh
        elif var == "rl":
            return self.__rl
        elif var == "x":
            return self.__x
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
        elif var == "hv_bus_id":
            self.__hv_bus_id = new
        elif var == "lv_bus_id":
            self.__lv_bus_id = new
        elif var == "hv_kv":
            self.__hv_kv = new
        elif var == "lv_kv":
            self.__lv_kv = new
        elif var == "sn_kva":
            self.__sn_kva = new
        elif var == "vk_percent":
            self.__vk_percent = new
        elif var == "vkr_percent":
            self.__vkr_percent = new
        elif var == "pfe_kw":
            self.__pfe_kw = new
        elif var == "i0_percent":
            self.__i0_percent = new
        elif var == "tap_min":
            self.__tap_min = new
        elif var == "tap_neutral":
            self.__tap_neutral = new
        elif var == "tap_max":
            self.__tap_max = new
        elif var == "tap_step_percent":
            self.__tap_step_percent = new
        elif var == "rh":
            self.__rh = new
        elif var == "rl":
            self.__rl = new
        elif var == "x":
            self.__x = new

        else:
            return "Not a valid variable for this element"

    def vk_to_t_and_x(self):
        pass

    def r_and_x_to_vk(self):
        pass
    
    def to_dict(self):
        """
        Convert threewindingtransformer attributes to a dictionary.

        :return: Dictionary representation of the object.
        :rtype: dict
        """
        return {
            "name": self.get_name(),
            "id": self.__id,
            "hv_bus_id": self.__hv_bus_id,
            "lv_bus_id": self.__lv_bus_id,
            "hv_kv": self.__hv_kv,
            "lv_kv": self.__lv_kv,
            "sn_kva": self.__sn_kva,
            "vk_percent": self.__vk_percent,
            "vkr_percent": self.__vkr_percent,
            "pfe_kw": self.__pfe_kw,
            "i0_percent": self.__i0_percent,
            "tap_min": self.__tap_min,
            "tap_neutral": self.__tap_neutral,
            "tap_max": self.__tap_max,
            "tap_step_percent": self.__tap_step_percent,
            "rh": self.__rh,
            "rl": self.__rl,
            "x": self.__x
        }
    


