
class Model(torch.nn.Module):
    def __init__(self, num_channel1=32, num_channel2=64):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(num_channel1, num_channel2, 1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.cat([v1] * 3)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(256, 32, 64, 64)
