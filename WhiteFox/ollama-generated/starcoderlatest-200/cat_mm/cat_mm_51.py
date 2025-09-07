
class Model(torch.nn.Module):
    def __init__(self, dim: int = 1024):
        super().__init__()
 
    def forward(self, x1: torch.Tensor, x2: torch.Tensor):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1, v1, ..., v1], dim=0)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
