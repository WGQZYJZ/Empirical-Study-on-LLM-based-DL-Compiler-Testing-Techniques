
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input = torch.randn(1, 8, 64)
 
    def forward(self, x1):
        v1  = torch.addmm(x1, self.mat1, self.mat2)
        v2 = torch.cat([v1], dim)
        return v2


# Inputs to the model
x1 = torch.randn(1, 8, 64)
mat1 = torch.randn(8, 5)
mat2 = torch.randn(5, 3)
