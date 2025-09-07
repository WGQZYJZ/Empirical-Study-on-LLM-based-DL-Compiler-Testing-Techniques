
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) + other
        v2  = torch.relu(v1)

# Initializing the model
m = Model()


# Inputs to the model
other  = torch.randn(3)
x1     = torch.randn(8, 3, 64, 64)
__output__  = m(x1)
