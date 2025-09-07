
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_1 = torch.nn.Conv2d(3, 8, 3, stride=2, padding=1)
        self.relu = torch.nn.ReLU()
        self.conv_2 = torch.nn.Conv2d(8, 16, 3, stride=2, padding=1)
 
    def forward(self, x):
        v1 = self.conv_1(x)
        v2 = self.relu(v1)
        v3 = self.conv_2(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
