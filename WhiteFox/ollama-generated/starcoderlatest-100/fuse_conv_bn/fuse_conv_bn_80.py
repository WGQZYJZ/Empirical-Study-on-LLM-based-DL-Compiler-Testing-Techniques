
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(2, 20, kernel_size=5)
        self.bn1 = torch.nn.BatchNorm2d(20)

    def forward(self, x):
        x = self.conv1(x)
        # Do not fuse the conv and bn layer now!
        x = self.bn1(x) 
        return x

# Inputs to the model
x = torch.randn(1, 3, 28, 28)
