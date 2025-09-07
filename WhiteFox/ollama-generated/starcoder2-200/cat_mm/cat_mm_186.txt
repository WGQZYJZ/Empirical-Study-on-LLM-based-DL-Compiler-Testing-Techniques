
class Model(torch.nn.Module):
    def __init__(self, shape01=[5, 4], shape23=6, axis=None):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1[0], x1[1])
        v2 = torch.cat([v1 for _ in range(shape01)], dim=axis)
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = [torch.randn((4, 5)), torch.randn((7, 8))]
__output__  = m(*x1)
 
