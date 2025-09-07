
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x1, x2)
        t1 = torch.cat([v1], dim=self.dim)
        return t1


# Initializing the model
m = Model(0)

# Inputs to the model
t1  = torch.randn(3, 5, 64, 64)
t2  = torch.randn(2, 8, 64, 64)
