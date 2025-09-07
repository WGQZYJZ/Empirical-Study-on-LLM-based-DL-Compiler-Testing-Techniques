
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, mat1, mat2):
        v1 = self.conv(x1)
        v2 = torch.addmm(v1, mat1, mat2)
        v3 = torch.cat([v2], dim)
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
mat1 = torch.randn(4, 8, 1, 1, requires_grad=True)
mat2 = torch.randn(4, 8, 2, 1, requires_grad=True)
