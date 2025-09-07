
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim
 
    def forward(self, x):
        v = torch.addmm(x[:, :self.dim], x[:, self.dim:], x[:, self.dim:])
        return v


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 8, 64, 64)
