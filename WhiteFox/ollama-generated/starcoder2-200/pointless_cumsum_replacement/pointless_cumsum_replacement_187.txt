
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
        v2 = convert_element_type(v1, dtype)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()
 
 # Inputs to the model
 __args__ = [torch.Tensor([arg1]), torch.Tensor([arg2])]
x1  = torch.randn(10*5*87)
__output__  = m(x1, *__args__)

