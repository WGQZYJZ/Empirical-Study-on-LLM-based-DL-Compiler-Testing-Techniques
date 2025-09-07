
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        t1 = torch.full([arg1, arg2], 1)
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()


# Inputs to the model
x1 = (5,) # This can be any valid input shape for tensor size as long as they match the pattern specified above.
