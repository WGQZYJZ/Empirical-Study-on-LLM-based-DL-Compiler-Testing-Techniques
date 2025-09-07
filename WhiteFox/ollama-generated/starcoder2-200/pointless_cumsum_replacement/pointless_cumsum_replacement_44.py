
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1):
        v1  = torch.full([arg1, 2], 3, dtype=dtype) # Create a tensor filled with the scalar value 10, with the specified dtype
        v2  = convert_element_type(v1, dtype)       # Convert the elements of the tensor to the specified dtype
        return torch.cumsum(v2, 1).div_(torch.ones([arg1], dtype=dtype))


# Initializing the model
m = Model()


# Inputs to the model
__output__  = m(3)
