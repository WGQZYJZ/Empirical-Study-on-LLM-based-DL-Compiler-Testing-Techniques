
class Model(nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, x2):
        return torch.cat([x1 * 0.5, x1 * 0.7071067811865476, torch.erf(x1 * 0.7071067811865476), (x2 + 1) * 0.7071067811865476, x2], dim=self.dim)


# Initializing the model
m = Model(dim=1)


# Inputs to the model
x1 = torch.randn(3, 4, 2, 2)
x2 = torch.randn(3, 8, 16, 16)
