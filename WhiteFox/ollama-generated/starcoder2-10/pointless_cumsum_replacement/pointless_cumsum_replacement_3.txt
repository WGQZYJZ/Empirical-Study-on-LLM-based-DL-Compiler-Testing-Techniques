
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        v0 = torch.full([arg1, arg2], 1, dtype=torch.int32)
        v1 = convert_element_type(v0, torch.float64) # Convert the elements of the tensor to double precision floating point numbers with a dynamic shape, by default the created tensor is 3D
        v2 = torch.cumsum(v1, dim=1) 
        return v2


# Initializing the model