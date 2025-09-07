
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1, arg1=None, arg2=None):
        if arg1 == 1:
            t1 = torch.full([arg1, arg2], 1, dtype=t1.dtype, layout=t1.layout, device=t1.device)
        if arg2 == 2:
            t3 = torch.cumsum(t2, 1)
        return t6


# Initializing the model
m = Model()
x1 = torch.randn(4, 8, 64, 64)
arg1 = x1.size()[0] if arg1 is None else arg1
arg2 = x1.size()[2] if arg2 is None else arg2
