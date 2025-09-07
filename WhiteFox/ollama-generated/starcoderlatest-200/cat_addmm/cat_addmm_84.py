
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.addmm(x1, t11, t12)
        v2 = torch.cat([v1], dim=0)
        return v2


# Initializing the model
m = Model()
# Inputs to the model
t11 = torch.randn(8, 3, 64, 64)
t12 = torch.randn(8, 3, 64, 64)
x1 = torch.randn(1, 3, 64, 64)
