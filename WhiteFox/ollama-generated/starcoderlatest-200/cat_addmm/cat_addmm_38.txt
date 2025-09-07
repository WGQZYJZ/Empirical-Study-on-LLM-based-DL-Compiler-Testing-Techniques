
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.mat_1 = torch.randn((16, 32))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.addmm(v1, self.mat_1, self.mat_2)
        return v2
 
m = Model()
x = torch.randn((1, 3, 64, 64))
