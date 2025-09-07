
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):  # The function takes in two parameters as arguments.
        v0 = torch.full([arg1, arg2], 1)
        v1 = convert_element_type(v0, dtype=dtype)
        v2 = torch.cumsum(v1, dim=1)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
__input1__, __input2__ = m.__next__(dtype=torch.int32), m.__next__(dtype=torch.double) 
