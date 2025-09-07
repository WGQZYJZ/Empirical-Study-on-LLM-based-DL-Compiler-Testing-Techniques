
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, arg1, arg2):
        t1 = torch.full([arg1, arg2], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device) 
        t2 = convert_element_type(t1, x1.dtype)
        t3 = torch.cumsum(t2, 1)
        return t3

# Inputs to the model
x1 = torch.randn(1, 8)
arg1 = x1.shape[0]
arg2 = x1.shape[1]
