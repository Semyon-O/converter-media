from abc import ABC, abstractmethod


class PhotoConverterStrategy(ABC):

    """This abstract class represents video converter strategy interface."""

    @abstractmethod
    def convert(self, input_file):

        """This method is responsible for converting using video strategy"""

        raise NotImplementedError


class PhotoConversionContext:

    """This class is responsible for converting video strategy interface"""

    def __init__(self, strategy: PhotoConverterStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PhotoConverterStrategy):
        if isinstance(strategy, PhotoConverterStrategy):
            self.strategy = strategy
        else:
            raise ValueError("Strategy must be an instance of VideoConverterStrategy")

    def convert(self, input_file):
        return self.strategy.convert(input_file)