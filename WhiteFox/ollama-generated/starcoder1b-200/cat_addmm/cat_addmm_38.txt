
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        mat1 = torch.randn((1, 2, 64, 64), requires_grad=True)
        mat2 = torch.randn((1, 2, 64, 64), requires_grad=True)
        mat3 = self.conv(x1) * 0.5 + mat1
        mat4 = self.conv(x1) * 0.7071067811865476 + mat2
        mat5 = torch.abs(mat3 - mat4).sqrt()
        mat6 = mat5.mul_(2) + mat3
        return mat6


# Initializing the model
m = Model()


