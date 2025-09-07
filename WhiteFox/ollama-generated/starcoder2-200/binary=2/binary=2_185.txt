
class Model(torch.nn.Module):
    def __init__(self, other1, other2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other1 * 0.7 + other2  # A constant is added to the output of 'other1' and then subtracted from the output of 'v1'. The 'other2' is not included in this pattern. 
        return v2


# Initializing the model
m = Model(torch.ones([3, 8, 64, 64]), torch.zeros([3]))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

