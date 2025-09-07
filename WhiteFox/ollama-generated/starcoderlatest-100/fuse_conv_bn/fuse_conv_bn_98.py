
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3)
        self.bn1 = torch.nn.BatchNorm2d(64)
        self.relu1 = torch.nn.ReLU()

    def forward(self, x):
        conv_out = self.conv1(x)
        bn_out = self.bn1(conv_out)
        out = self.relu1(bn_out)
        return out
# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
