
class Model(torch.nn.Module):
    def __init__(self, hidden_size=8):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, hidden_size, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = self.conv1(x)
        v = v * 0.5
        v = self.conv2(v)
        return v


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
