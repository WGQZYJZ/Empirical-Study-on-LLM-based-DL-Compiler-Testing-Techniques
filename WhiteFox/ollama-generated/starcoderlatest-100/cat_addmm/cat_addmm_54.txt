
class Model(torch.nn.Module):
    def __init__(self, mat1, mat2):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.mat1, self.mat2)
        v2 = torch.cat([v1], dim=3)
        return v2


# Initializing the model and inputs to the model
m = Model(torch.randn(8), torch.randn(8))
x1 = torch.randn(1, 8, 64, 64)
