
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):  # Initialize with arguments
        v1 = torch.full([arg1, arg2], 1) 
        v2 = convert_element_type(v1, dtype=torch.float32)
        v3 = torch.cumsum(v2, dim=1)
 
        return v3

# Initializing the model with arguments
m = Model()

# Inputs to the model with arguments 1 and 2 are provided by the user
x1, x2 = 50, 5

