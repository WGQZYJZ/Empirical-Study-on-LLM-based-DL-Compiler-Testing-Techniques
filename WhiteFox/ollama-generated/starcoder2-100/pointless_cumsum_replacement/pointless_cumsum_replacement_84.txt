
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0):
        arg1 = 5
        arg2 = torch.Size([3])
        v1  = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False) 
        v2  = convert_element_type(v1, dtype)
        v3  = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x0  = torch.randn(5, 3)
__output__  = m(x0)