
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=3) # The convolution is performed first in conv2d and then fused into a single conv layer
        self.batch_norm = torch.nn.BatchNorm2d(8)

    def forward(self, x1):
        output = self.conv1(x1)
        