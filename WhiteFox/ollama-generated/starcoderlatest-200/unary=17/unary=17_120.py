
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 16, stride=4, padding=2)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m2 = Model2()


# Inputs to the model
x2 = torch.randn(32, 3, 64, 64)
