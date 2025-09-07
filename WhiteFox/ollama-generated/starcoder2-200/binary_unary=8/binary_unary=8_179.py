
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        return torch.relu(v2)


m2 = Model()
x2 = torch.randn(1, 3, 64, 64)
output__m2  = m2(x2)
m3 = Model2()
__output__m3 = m3(x2)
