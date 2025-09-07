
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 4, stride=2, padding=0)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        return v2


# Inputs to the model
inputs = [torch.randn(3, 8, 64, 64), torch.randn(8, 16, 64, 64)]
