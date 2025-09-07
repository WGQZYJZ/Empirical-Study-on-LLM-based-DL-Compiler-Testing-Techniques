
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.relu = torch.nn.ReLU()
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
 
    def forward(self, x):
        # (batch, channel, height, width)
        x = self.relu(self.conv1(x))  # (batch, 16, height, width)
        x = self.relu(self.conv2(x))  # (batch, 16, height, width)
        return x

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
