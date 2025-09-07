 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, kernel_size=(3, 3))
        self.bn1 = torch.nn.BatchNorm2d(64)

        self.conv2 = torch.nn.Conv2d(64, 64, kernel_size=(3, 3), stride=(2, 2))
        self.bn2 = torch.nn.BatchNorm2d(64)

    def forward(self, x1):
        y1 = torch.nn.functional.relu(torch.nn.functional.conv2d(x1, self.conv1.weight, self.conv1.bias))
        y2 = torch.nn.functional.max_pool2d(y1, kernel_size=(3, 3), stride=2)
        y2 = torch.nn.functional.relu(torch.nn.functional.batch_norm(y2))
        y3 = torch.nn.functional.conv2d(y2, self.conv2.weight, self.conv2.bias)

        # Fusing 1st and 2nd convolution layers to conv1 with same weight, conv2's bias set to zero
        conv = torch.nn.Conv2d(3, 64, kernel_size=(3, 3))
        bn = torch.nn.BatchNorm2d(64)

        y4 = self.conv1(x1)
        z1 = conv(y1) + self.conv2(y2) # Output shape: [batch, c, in_h/s, in_w/s]
        x2 = bn(z1, y3) # Output shape: [batch, c, h/s, w/s]
        y5 = torch.nn.functional.conv2d(x2, self.bn1.weight, bias=None) + y4

        return y5

# Initializing the model
m = Model()
__input__ = torch.randn(1, 3, 28, 28)

