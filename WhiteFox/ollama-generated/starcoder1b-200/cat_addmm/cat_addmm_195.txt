
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.randn(2, 4)
        self.mat2 = torch.randn(3, 4)
 
    def forward(self, x1, x2):
        v1 = torch.matmul(x1, self.mat1)
        v2 = torch.cat([v1], dim=-1)
        v3 = torch.addmm(v2, x2, self.mat2)
        return v3


# Inputs to the model
x1 = torch.randn(2, 4)
x2 = torch.randn(3, 4)
