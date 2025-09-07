
class Model(torch.nn.Module):
    def __init__(self, channel_in, channel_out):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(channel_in, 32, 3, stride=2)
        self.conv2 = torch.nn.Conv2d(64, 64, 3, stride=2)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        return [v1, v2]


# Initializing the model
m = Model(channel_in=64, channel_out=80)

# Inputs to the model
x = torch.randn(1, 3, 576, 576)
