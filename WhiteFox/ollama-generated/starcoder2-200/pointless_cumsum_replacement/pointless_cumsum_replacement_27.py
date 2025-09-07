
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        v1  = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device)
        v2  = convert_element_type(v1, dtype) 
        v3  = torch.cumsum(v2, 1) 
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
input0  = torch.rand(arg1=5, arg2=8) # random input tensor with shape [5, 8]
__output__  = m(input0, arg2=6)

