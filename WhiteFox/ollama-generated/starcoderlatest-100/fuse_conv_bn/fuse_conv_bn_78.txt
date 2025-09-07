
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)
        self.bn1 = torch.nn.BatchNorm2d(64)

        self.conv2 = torch.nn.Conv2d(in_channels=64, out_channels=32, kernel_size=3)
        self.bn2 = torch.nn.BatchNorm2d(32)

    def forward(self, x):
        v1  = torch.nn.functional.conv2d(x, self.conv1.weight, bias=None, stride=(1, 1), padding=(1, 1))
        v1 += self.bn1(v1)
        v2  = torch.nn.functional.conv2d(v1, self.conv2.weight, bias=None, stride=(1, 1), padding=(1, 1))
        v2 += self.bn2(v2)

        return v2

# Initializing the model
m = Model()

 # Inputs to the model
 x = torch.randn(1, 3, 56, 56)
 