
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        t1 = torch.mm(x1, x1)
        t2 = x1 * x1
        t3 = t1 * t2
        return torch.cat([t3], 1)


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
