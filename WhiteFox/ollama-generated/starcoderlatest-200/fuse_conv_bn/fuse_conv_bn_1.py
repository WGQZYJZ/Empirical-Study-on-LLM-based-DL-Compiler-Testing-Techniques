
class Model(torch.nn.Module):
    def __init__(self, stride=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 6, kernel_size=(5, 3), stride=stride)
        self.bn = torch.nn.BatchNorm2d(6)

    def forward(self, x1):
        # The conv layer must be in evaluation mode and have training statistics
        v1 = self.conv(x1).eval().batch_norm(self.bn(x1))
        return v1
