
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.conv2 = torch.nn.Conv2d(8, 16, 3)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
 
        return v2


# Initializing the model
m = Model2()
 
# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
