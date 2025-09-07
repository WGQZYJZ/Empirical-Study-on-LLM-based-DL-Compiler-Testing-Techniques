
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        v0 = torch.split(x1, [2], self.dim)
        v1 = torch.cat([v0[i] for i in range(len(v0))])
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
