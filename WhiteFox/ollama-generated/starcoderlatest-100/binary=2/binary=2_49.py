
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v2


# Initializing the model
m2 = Model2()

# Inputs to the model
x1_2 = torch.randn(1, 3, 64, 64)
other = 0.5
