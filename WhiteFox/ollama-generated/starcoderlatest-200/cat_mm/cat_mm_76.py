
class Model(torch.nn.Module):
    def __init__(self, dim: int = 1):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1: torch.Tensor, x2: torch.Tensor):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1] * self.dim)
        return v2


# Initializing the model
m = Model(dim=3)
# Inputs to the model
x1 = torch.randn(4, 8, 5, 10)
x2 = torch.randn(8, 16, 10, 5)
