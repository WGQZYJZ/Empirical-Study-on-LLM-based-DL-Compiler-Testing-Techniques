
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(3, 8, kernel_size=5)
        self.conv2  = torch.nn.ConvTranspose2d(32, 16, kernel_size=4, stride=2, padding=0)
    def forward(self, x):
        v1 = F.relu(self.conv1(x))
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = self.conv2(v4) / 6
        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 79, 79)
