
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, arg2=2):
        t0 = torch.full([x1], 1, dtype=x1.dtype)
        t1 = convert_element_type(t0, arg2)
        t2 = torch.cumsum(t1, 0)
        return t2


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64, device='cpu')
