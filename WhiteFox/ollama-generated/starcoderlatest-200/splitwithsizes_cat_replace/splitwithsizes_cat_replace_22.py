
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        x2  = torch.split(x1, 16, dim=self.dim)
        return torch.cat([x3 for x3 in x2], dim=self.dim)


# Inputs to the model
x1 = torch.randn(8, 10, 512, 512)
