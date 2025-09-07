
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        v1 = torch.full([arg1, arg2], 1)
        v2 = convert_element_type(v1, torch.int32)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
__args0__ = [4]
__args1__ = [8]
x2_shape = (torch.Size(__args0__), torch.Size(__args1__))
x3 = torch.randn(x2_shape)
__output__  = m(x3, x2_shape[-2:])

