
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        v1 = torch.full([arg1, arg2], 1, dtype=torch.int8) 
        v2 = convert_element_type(v1, torch.float64) 
        v3 = torch.cumsum(v2, 0)
        return v3

# Initializing the model
m = Model()
 
# Inputs to the model
arg1 = 5
arg2 = 64
