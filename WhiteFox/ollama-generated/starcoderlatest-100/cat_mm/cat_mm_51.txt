
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        t1 = torch.cat([v1, v1, 0], dim=1) 
        return t1


# Inputs to the model
x1 = torch.randn(48, 3, 64, 64)
x2 = torch.randn(6, 8, 64, 64)
