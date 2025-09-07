
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.randn(10, 3)
        self.mat2 = torch.randn(40, 16)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.mat1, self.mat2)
        v2 = torch.cat([v1], dim=1)
        return v2
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
