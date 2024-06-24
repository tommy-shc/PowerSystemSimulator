#ThreeWindingTransformer Class
#May 30, 2024

from networks.Element import Element

class ThreeWindingTransformer(Element):
    """
    Represents a three-winding transformer element in a power system network.
    
    :param name: The name of the three-winding transformer.
    :type name: str
    :param hv_bus_id: The ID of the high-voltage (HV) bus where the transformer is connected.
    :type hv_bus_id: int
    :param mv_bus_id: The ID of the medium-voltage (MV) bus where the transformer is connected.
    :type mv_bus_id: int
    :param lv_bus_id: The ID of the low-voltage (LV) bus where the transformer is connected.
    :type lv_bus_id: int
    :param hv_kv: The high-voltage (HV) rating of the transformer in kilovolts (kV).
    :type hv_kv: float
    :param mv_kv: The medium-voltage (MV) rating of the transformer in kilovolts (kV).
    :type mv_kv: float
    :param lv_kv: The low-voltage (LV) rating of the transformer in kilovolts (kV).
    :type lv_kv: float
    :param sn_hv_kva: The apparent power rating of the transformer at high voltage (HV) side in kilovolt-amperes (kVA).
    :type sn_hv_kva: float
    :param sn_mv_kva: The apparent power rating of the transformer at medium voltage (MV) side in kilovolt-amperes (kVA).
    :type sn_mv_kva: float
    :param sn_lv_kva: The apparent power rating of the transformer at low voltage (LV) side in kilovolt-amperes (kVA).
    :type sn_lv_kva: float
    :param vk_hv_percent: The short-circuit voltage percentage of the transformer at high voltage (HV) side.
    :type vk_hv_percent: float
    :param vk_mv_percent: The short-circuit voltage percentage of the transformer at medium voltage (MV) side.
    :type vk_mv_percent: float
    :param vk_lv_percent: The short-circuit voltage percentage of the transformer at low voltage (LV) side.
    :type vk_lv_percent: float
    :param vkr_hv_percent: The short-circuit voltage resistance percentage of the transformer at high voltage (HV) side.
    :type vkr_hv_percent: float
    :param kr_mv_percent: The short-circuit voltage resistance percentage of the transformer at medium voltage (MV) side.
    :type kr_mv_percent: float
    :param vkr_lv_percent: The short-circuit voltage resistance percentage of the transformer at low voltage (LV) side.
    :type vkr_lv_percent: float
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
    :param rm: Resistance at medium voltage (MV) side of the transformer.
    :type rm: float
    :param rl: Resistance at low voltage (LV) side of the transformer.
    :type rl: float
    :param xh: Reactance at high voltage (HV) side of the transformer.
    :type xh: float
    :param xm: Reactance at medium voltage (MV) side of the transformer.
    :type xm: float
    :param xl: Reactance at low voltage (LV) side of the transformer.
    :type xl: float
    """

    _next_id = 1

    def __init__(self, name: str, hv_bus_id: int, mv_bus_id: int, lv_bus_id: int, hv_kv: float, mv_kv: float, lv_kv: float, sn_hv_kva: float, sn_mv_kva: float, sn_lv_kva: float, vk_hv_percent: float, vk_mv_percent: float, vk_lv_percent: float, vkr_hv_percent: float, vkr_mv_percent: float, vkr_lv_percent: float, pfe_kw: float, i0_percent: float, tap_min: float, tap_neutral: float, tap_max: float, tap_step_percent: float, rh: float, rm: float, rl: float, xh: float, xm: float, xl: float):
        
        """
        Initializes a three-winding transformer element in a power system network.
        
        :param name: The name of the three-winding transformer.
        :type name: str
        :param hv_bus_id: The ID of the high-voltage (HV) bus where the transformer is connected.
        :type hv_bus_id: int
        :param mv_bus_id: The ID of the medium-voltage (MV) bus where the transformer is connected.
        :type mv_bus_id: int
        :param lv_bus_id: The ID of the low-voltage (LV) bus where the transformer is connected.
        :type lv_bus_id: int
        :param hv_kv: The high-voltage (HV) rating of the transformer in kilovolts (kV).
        :type hv_kv: float
        :param mv_kv: The medium-voltage (MV) rating of the transformer in kilovolts (kV).
        :type mv_kv: float
        :param lv_kv: The low-voltage (LV) rating of the transformer in kilovolts (kV).
        :type lv_kv: float
        :param sn_hv_kva: The apparent power rating of the transformer at high voltage (HV) side in kilovolt-amperes (kVA).
        :type sn_hv_kva: float
        :param sn_mv_kva: The apparent power rating of the transformer at medium voltage (MV) side in kilovolt-amperes (kVA).
        :type sn_mv_kva: float
        :param sn_lv_kva: The apparent power rating of the transformer at low voltage (LV) side in kilovolt-amperes (kVA).
        :type sn_lv_kva: float
        :param vk_hv_percent: The short-circuit voltage percentage of the transformer at high voltage (HV) side.
        :type vk_hv_percent: float
        :param vk_mv_percent: The short-circuit voltage percentage of the transformer at medium voltage (MV) side.
        :type vk_mv_percent: float
        :param vk_lv_percent: The short-circuit voltage percentage of the transformer at low voltage (LV) side.
        :type vk_lv_percent: float
        :param vkr_hv_percent: The short-circuit voltage resistance percentage of the transformer at high voltage (HV) side.
        :type vkr_hv_percent: float
        :param vkr_mv_percent: The short-circuit voltage resistance percentage of the transformer at medium voltage (MV) side.
        :type vkr_mv_percent: float
        :param vkr_lv_percent: The short-circuit voltage resistance percentage of the transformer at low voltage (LV) side.
        :type vkr_lv_percent: float
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
        :param rm: Resistance at medium voltage (MV) side of the transformer.
        :type rm: float
        :param rl: Resistance at low voltage (LV) side of the transformer.
        :type rl: float
        :param xh: Reactance at high voltage (HV) side of the transformer.
        :type xh: float
        :param xm: Reactance at medium voltage (MV) side of the transformer.
        :type xm: float
        :param xl: Reactance at low voltage (LV) side of the transformer.
        :type xl: float
        """
        
        super().__init__(name)
        self.__id = ThreeWindingTransformer._next_id
        self.__hv_bus_id =hv_bus_id
        self.__mv_bus_id =mv_bus_id
        self.__lv_bus_id =lv_bus_id
        self.__hv_kv =hv_kv
        self.__mv_kv =mv_kv
        self.__lv_kv =lv_kv
        self.__sn_hv_kva =sn_hv_kva
        self.__sn_mv_kva =sn_mv_kva
        self.__sn_lv_kva =sn_lv_kva
        self.__vk_hv_percent =vk_hv_percent
        self.__vk_mv_percent =vk_mv_percent
        self.__vk_lv_percent =vk_lv_percent
        self.__vkr_hv_percent =vkr_hv_percent
        self.__vkr_mv_percent =vkr_mv_percent
        self.__vkr_lv_percent =vkr_lv_percent
        self.__pfe_kw =pfe_kw
        self.__i0_percent =i0_percent
        self.__tap_min =tap_min
        self.__tap_neutral =tap_neutral
        self.__tap_max =tap_max
        self.__tap_step_percent =tap_step_percent
        self.__rh =rh
        self.__rm =rm 
        self.__rl =rl 
        self.__xh =xh
        self.__xm =xm
        self.__xl =xl
        
        ThreeWindingTransformer._next_id += 1


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
        elif var == "mv_bus_id":
            return self.__mv_bus_id
        elif var == "lv_bus_id":
            return self.__lv_bus_id
        elif var == "hv_kv":
            return self.__hv_kv
        elif var == "mv_kv":
            return self.__mv_kv
        elif var == "lv_kv":
            return self.__lv_kv
        elif var == "sn_hv_kva":
            return self.__sn_hv_kva
        elif var == "sn_mv_kva":
            return self.__sn_mv_kva
        elif var == "sn_lv_kva":
            return self.__sn_lv_kva
        elif var == "vk_hv_percent":
            return self.__vk_hv_percent
        elif var == "vk_mv_percent":
            return self.__vk_mv_percent
        elif var == "vk_lv_percent":
            return self.__vk_lv_percent
        elif var == "vkr_hv_percent":
            return self.__vkr_hv_percent
        elif var == "vkr_mv_percent":
            return self.__vkr_mv_percent
        elif var == "vkr_lv_percent":
            return self.__vkr_lv_percent
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
        elif var == "rm":
            return self.__rm
        elif var == "rl":
            return self.__rl
        elif var == "xh":
            return self.__xh
        elif var == "xm":
            return self.__xm
        elif var == "xl":
            return self.__xl
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
        elif var == "mv_bus_id":
            self.__mv_bus_id = new
        elif var == "lv_bus_id":
            self.__lv_bus_id = new
        elif var == "hv_kv":
            self.__hv_kv = new
        elif var == "mv_kv":
            self.__mv_kv = new
        elif var == "lv_kv":
            self.__lv_kv = new
        elif var == "sn_hv_kva":
            self.__sn_hv_kva = new
        elif var == "sn_mv_kva":
            self.__sn_mv_kva = new
        elif var == "sn_lv_kva":
            self.__sn_lv_kva = new
        elif var == "vk_hv_percent":
            self.__vk_hv_percent = new
        elif var == "vk_mv_percent":
            self.__vk_mv_percent = new
        elif var == "vk_lv_percent":
            self.__vk_lv_percent = new
        elif var == "vkr_hv_percent":
            self.__vkr_hv_percent = new
        elif var == "vkr_mv_percent":
            self.__vkr_mv_percent = new
        elif var == "vkr_lv_percent":
            self.__vkr_lv_percent = new
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
        elif var == "rm":
            self.__rm = new
        elif var == "rl":
            self.__rl = new
        elif var == "xh":
            self.__xh = new
        elif var == "xm":
            self.__xm = new
        elif var == "xl":
            self.__xl = new
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
            "mv_bus_id": self.__mv_bus_id,
            "lv_bus_id": self.__lv_bus_id,
            "hv_kv": self.__hv_kv,
            "mv_kv": self.__mv_kv,
            "lv_kv": self.__lv_kv,
            "sn_hv_kva": self.__sn_hv_kva,
            "sn_mv_kva": self.__sn_mv_kva,
            "sn_lv_kva": self.__sn_lv_kva,
            "vk_hv_percent": self.__vk_hv_percent,
            "vk_mv_percent": self.__vk_mv_percent,
            "vk_lv_percent": self.__vk_lv_percent,
            "vkr_hv_percent": self.__vkr_hv_percent,
            "vkr_mv_percent": self.__vkr_mv_percent,
            "vkr_lv_percent": self.__vkr_lv_percent,
            "pfe_kw": self.__pfe_kw,
            "i0_percent": self.__i0_percent,
            "tap_min": self.__tap_min,
            "tap_neutral": self.__tap_neutral,
            "tap_max": self.__tap_max,
            "tap_step_percent": self.__tap_step_percent,
            "rh": self.__rh,
            "rm": self.__rm,
            "rl": self.__rl,
            "xh": self.__xh,
            "xm": self.__xm,
            "xl": self.__xl 
        }
