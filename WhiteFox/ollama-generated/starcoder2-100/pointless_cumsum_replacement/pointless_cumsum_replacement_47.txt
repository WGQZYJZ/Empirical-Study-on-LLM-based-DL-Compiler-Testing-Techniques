
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.full([x1 + 1, x2 - 2], 1) # Create a tensor filled with the scalar value 1, with the size of dimension [3] and device
        v2  = convert_element_type(v1, torch.float32)
        v3  = torch.cumsum(v2, 1)
        return v3

# Initializing the model
m  = Model()
__output___1__  = m(__input_arg1__, __input_arg2__)

# Inputs to the model