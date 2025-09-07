
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, mat1, mat2):
        v1 = self.conv(x1)
        v2 = torch.addmm(v1, mat1, mat2)
        return v2


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
mat1 = torch.randn(1, 8, 32, 32)
mat2 = torch.randn(1, 8, 64, 64)
