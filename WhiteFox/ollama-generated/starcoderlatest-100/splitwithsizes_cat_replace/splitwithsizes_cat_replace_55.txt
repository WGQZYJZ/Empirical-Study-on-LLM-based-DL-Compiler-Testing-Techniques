
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.pool = torch.nn.MaxPool2d(2, stride=2, ceil_mode=True)
 
    def forward(self, x):
        s1 = self.conv1(x)
        s2 = self.pool(s1)
        return s2

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
