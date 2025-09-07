
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, 0:size]
        return v2


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 5, 8, 8)
__output__  = m(x1, x2)


