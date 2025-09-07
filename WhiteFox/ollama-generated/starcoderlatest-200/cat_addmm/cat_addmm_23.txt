
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.nn.Parameter(torch.randn(1, 64, 64))
        self.mat2 = torch.nn.Parameter(torch.randn(1, 64, 64))
 
    def forward(self, x):
        v1 = torch.addmm(x, self.mat1, self.mat2)
        v2 = torch.cat([v1], dim=0)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 64, 64)
