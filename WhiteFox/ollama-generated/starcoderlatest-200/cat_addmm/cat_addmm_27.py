
class Model(torch.nn.Module):
    def __init__(self, dim: int=1):
        super().__init__()
 
    def forward(self, x):
        v1 = torch.addmm(x, torch.eye(3), torch.ones(3))
        t1 = torch.cat([v1], dim)
        return t1


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(4, 2)
