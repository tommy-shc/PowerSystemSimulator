from abc import ABC, abstractmethod

class Element(ABC):
    """
    An abstract base class representing an element in a network.
    """
    def __init__(self, name: str):
        """
        Initializes an Element object.

        :param name: The name of the element.
        :type name: str
        """
        self.__name = name

    def get_name(self):
        """
        Get the name of the element.

        :return: The name of the element.
        :rtype: str
        """
        return self.__name
    
    def set_name(self, n: str):
        """
        Set the name of the element.

        :param n: The new name for the element.
        :type n: str
        """
        self.__name = n
        return
    
    @abstractmethod
    def get_property(self):
        """
        Abstract method to get a property of the element.

        This method must be implemented by subclasses.

        :raises NotImplementedError: If not implemented by subclass.
        """
        pass

    @abstractmethod
    def set_property(self):
        """
        Abstract method to set a property of the element.

        This method must be implemented by subclasses.

        :raises NotImplementedError: If not implemented by subclass.
        """
        pass

    @abstractmethod
    def to_dict(self):
        """
        Abstract method to convert object attributes to a dictionary.

        This method must be implemented by subclasses.

        :raises NotImplementedError: If not implemented by subclass.
        """
        pass