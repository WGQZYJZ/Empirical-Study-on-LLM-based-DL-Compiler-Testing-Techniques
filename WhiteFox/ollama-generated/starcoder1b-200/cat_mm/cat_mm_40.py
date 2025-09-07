
class Model(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Compute the output of the matrix multiplication operation along the specified dimension `self.dim`
        return torch.cat([v1, v1, ..., v1], dim=self.dim)


# Inputs to the model
x1  = torch.randn(3, 4, 64, 64)
x2  = torch.randn(3, 4, 64, 64)
