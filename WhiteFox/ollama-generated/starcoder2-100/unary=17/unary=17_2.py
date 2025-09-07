
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        v  = self.conv(x)
        v1 = torch.relu(v)
        return v1


m = Model2()
x1 = torch.randn(1,3,64,64)
