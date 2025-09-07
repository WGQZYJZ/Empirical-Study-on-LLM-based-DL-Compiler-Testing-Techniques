
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2.t(), x2)
        v2 = torch.cat([v1], dim=dim)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4)
x2 = torch.randn(2, 3)
