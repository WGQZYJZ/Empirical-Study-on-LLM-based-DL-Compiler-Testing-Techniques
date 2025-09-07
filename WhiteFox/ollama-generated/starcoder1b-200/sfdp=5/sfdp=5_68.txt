
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0, dilation=2)
 
    def forward(self, x):
        v1 = F.gelu(self.conv1(x))
        v2 = self.conv2(v1)
        return torch.tanh(v2)


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(4, 3, 64, 64)
