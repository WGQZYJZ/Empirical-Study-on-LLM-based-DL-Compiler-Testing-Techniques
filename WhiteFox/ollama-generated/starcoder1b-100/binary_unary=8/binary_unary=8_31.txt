
class Model(torch.nn.Module):
    def __init__(self, in_channel, out_channel):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channel, out_channel, 3, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        return v1 + 0.5


# Inputs to the model
x1 = torch.randn(1, 64, 64, in_channel)
