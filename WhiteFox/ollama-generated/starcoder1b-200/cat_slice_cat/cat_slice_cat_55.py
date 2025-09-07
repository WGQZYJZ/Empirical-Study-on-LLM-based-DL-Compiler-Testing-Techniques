
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1, stride=1, padding=0)
 
    def forward(self, x):
        v = torch.cat([x[:, 0:32], x[:, 0:32]], dim=1)
        v = self.conv1(v)
        v = self.conv2(v)
        return v


# Inputs to the model
x = torch.randn(2, 3, 64, 64)
