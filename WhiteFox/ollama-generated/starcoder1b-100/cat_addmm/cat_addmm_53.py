
class Model(torch.nn.Module):
    def __init__(self, num_output):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = x + 1
        conv1_output  = self.conv1(v)
        conv2_output  = self.conv2(conv1_output)
        return conv2_output

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
y  = x1 + 1
__output1__ = Model()(x1)
__output2__ = Model()(x1 + y)

