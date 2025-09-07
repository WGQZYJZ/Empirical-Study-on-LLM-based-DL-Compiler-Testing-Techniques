
class Model(torch.nn.Module):
    def __init__(self, layer1, layer2):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, layer1, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(layer1, layer2, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        return torch.relu(v3)


# Initializing the model
m  = Model(layer_size=4, channel_size=8)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
