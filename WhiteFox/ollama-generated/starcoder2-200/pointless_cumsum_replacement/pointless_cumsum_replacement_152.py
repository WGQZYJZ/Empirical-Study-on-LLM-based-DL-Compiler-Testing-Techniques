
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2, dtype=None): # The function should have 3 inputs and the last input is optional
        t1 = torch.full([arg1, arg2], 1, dtype=dtype)
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, 1)

# Initializing the model
m = Model()

 # Inputs to the model
__args__ = (1000,) * m.forward.__code__.co_argcount
  # The first input is an integer and the second one is 64 by default for the 3rd argument, and 256 as a default value for the 7th argument.
__args__[0] = 18
__args__[1] = 32

 # Initializing the model with arguments to override
