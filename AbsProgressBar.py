import math
class AbsProgressBar:
    """Creates a progress bar, with the ability to specify the maximum buffer size and the size of the progress bar"""
    # Author https://github.com/MrAbsurdick
    def __init__(self, max_value:int=100, size_line:int=100, no_limit:bool=False) -> None:
        self.max_value = max_value # Maximum value
        self.no_limit = no_limit # Allows you to exceed the maximum value

        self.value = 0 # present value
        self.step = self.max_value / size_line # The size of one step in the progress bar

        self.S_Load_0 = '█' # Load Line Symbol
        self.S_Load_3 = '░' # Load Line Symbol
        
        self.__calc = lambda value: round(self.value + value, 3)

    def update(self, value:int) -> bool:
        """Changing the progress value"""
        # If (no_limit==True) perform action
        if self.no_limit:
            self.value = self.__calc(value)
            return True
        # If the maximum value is not exceeded
        elif 0 <= (__value:=self.__calc(value)) <= self.max_value:
            self.value = __value
            return True
        # If none of the conditions are met
        else:
            return False
        

    def display(self) -> None:
        """Display progress bar on screen"""
        # check whether the maximum value of the <S_Load_0>line size is exceeded
        if self.value <= self.max_value:
            left = self.S_Load_0*math.ceil(self.value/self.step)
        else:
            left = self.S_Load_0*math.ceil(self.max_value/self.step)
        # check whether the maximum value of the <S_Load_3>line size is exceeded
        if self.value >= 0:
            right = self.S_Load_3*math.floor((self.max_value-self.value)/self.step)
        else:
            right = self.S_Load_3*math.floor(self.max_value/self.step)
        # Display result on screen
        print(f"\r{left}{right} [{self.value}/{self.max_value}]", end="\t", flush=True)