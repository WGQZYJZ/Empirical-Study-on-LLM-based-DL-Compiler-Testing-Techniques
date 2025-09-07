
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.mat1 = torch.randn(8, 32)
        self.mat2 = torch.randn(16, 32)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.mat1, self.mat2)
        v2 = torch.cat([v1], dim=dim)
        return v2


# Initializing the model
m = Model(3)
# Inputs to the model
x1 = torch.randn(8, 32)
