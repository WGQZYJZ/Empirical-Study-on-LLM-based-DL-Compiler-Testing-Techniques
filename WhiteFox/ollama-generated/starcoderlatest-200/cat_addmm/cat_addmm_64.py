
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.addmm = torch.nn.Linear(dim, dim)
 
    def forward(self, x):
        v1 = self.addmm(x)
        v2 = torch.cat([v1], 1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
