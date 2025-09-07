
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.other1 = 4 # any nonzero number
        self.conv2 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = v1 + self.other1
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x_  = torch.randn(1, 3, 64, 64)
__output___ = m(x_)

