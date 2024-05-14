from abc import ABC, abstractmethod


class AudioConverterStrategy(ABC):

    """This abstract class represents video converter strategy interface."""

    @abstractmethod
    def convert(self, input_file):

        """This method is responsible for converting using video strategy"""

        raise NotImplementedError


class AudioConversionContext:

    """This class is responsible for converting video strategy interface"""

    def __init__(self, strategy: AudioConverterStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: AudioConverterStrategy):
        if isinstance(strategy, AudioConverterStrategy):
            self.strategy = strategy
        else:
            raise ValueError("Strategy must be an instance of VideoConverterStrategy")

    def convert(self, input_file):
        return self.strategy.convert(input_file)