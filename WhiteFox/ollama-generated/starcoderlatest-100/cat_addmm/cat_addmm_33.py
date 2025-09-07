
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mat1 = torch.randn(8, 256, 3, 3)
        self.mat2 = torch.randn(256, 512, 4, 4)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, self.mat1, self.mat2)
        v2 = torch.cat([v1], dim=-3)
        return v2


# Inputs to the model
x1 = torch.randn(256, 2048, 4, 4)
