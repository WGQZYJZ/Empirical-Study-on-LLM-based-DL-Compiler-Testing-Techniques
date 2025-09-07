
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        x2 = torch.split(x1, 4, self.dim)
        x3 = torch.cat([x for i in range(len(x2))], self.dim)
        return x3


# Initializing the model
m = Model(dim=0)

# Inputs to the model
x1 = torch.randn(64, 64, 64)
