
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        v1  = torch.split(x1, 2, self.dim) 
        v2  = torch.cat([v1[i] for i in range(len(v1))], dim=self.dim) 
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
