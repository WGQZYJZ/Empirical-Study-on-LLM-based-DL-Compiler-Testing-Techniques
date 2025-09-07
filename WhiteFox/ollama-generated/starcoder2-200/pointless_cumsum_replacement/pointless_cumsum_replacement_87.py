
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        v1  = torch.full([arg1, arg2], 1, dtype=torch.int64)
        v2  = convert_element_type(v1, torch.double) # Convert the elements of the tensor to double precision floating-point numbers
        v3  = torch.cumsum(v2, dim=1)
        return v3

# Initializing model
m  = Model()

# Inputs to the model
arg1, arg2  = (20,) # Dimensions of the input tensor
__output__  = m(*([arg1]*5), *([arg2]*4))

