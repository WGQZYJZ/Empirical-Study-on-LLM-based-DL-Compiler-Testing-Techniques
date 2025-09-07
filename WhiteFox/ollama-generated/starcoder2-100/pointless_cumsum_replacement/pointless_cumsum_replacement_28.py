
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1):
        v1  = torch.full([arg1], 32768) 
        v2  = convert_element_type(v1, 0) # Change data type of v1 from int to float
        v3  = torch.cumsum(v2, axis=0)
        return v3

# Initializing the model
m = Model()

# Inputs to the model
arg1 = 4

