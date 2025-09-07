
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, 5) # 6 x 6
        self.conv2 = torch.nn.Conv2d(4, 8, 7) # 4 x 4

    def forward(self, x):
        x1 = F.relu(self.conv1(x)) # 30 x 30
        x2 = F.relu(self.conv2(x1)) # 26 x 26
        return x2
# Initializing the model
m = Model()
# Inputs to the model
x = torch.randn(1, 3, 14, 14)
