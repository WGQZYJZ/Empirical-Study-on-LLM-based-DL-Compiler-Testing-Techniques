
class ConvModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, kernel_size=3)
        self.bn   = torch.nn.BatchNorm2d(num_features=3)

    def forward(self, x1):
        conv = self.conv(x1)
        bn = self.bn(conv)
        return conv

model = ConvModel()

