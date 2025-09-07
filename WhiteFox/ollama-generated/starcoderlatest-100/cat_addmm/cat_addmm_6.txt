
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, x2):
        v1  = torch.addmm(x1, self.weight1, self.weight2)
        v2  = torch.cat([v1], dim=self.dim)
        return v2


# Initializing the model and its parameters
m = Model(0)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(8, 1)
