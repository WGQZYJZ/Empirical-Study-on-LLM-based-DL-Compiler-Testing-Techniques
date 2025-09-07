
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        t1 = torch.split(x1, self.dim, 3)
        t2 = torch.cat([t for i in range(len(t1))], dim=3)
        return t2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
