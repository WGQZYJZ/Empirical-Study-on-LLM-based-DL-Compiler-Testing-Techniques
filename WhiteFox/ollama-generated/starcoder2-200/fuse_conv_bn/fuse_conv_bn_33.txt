
import torch

class Model(torch.nn.Module):
    def __init__(self, num_channels):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(num_channels, 64, kernel_size=3)
        self.bn1   = torch.nn.BatchNorm2d(64)
        self.conv2 = torch.nn.Conv2d(64, 64, kernel_size=3)
        self.relu  = torch.nn.ReLU()

    def forward(self, x):
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out) # Fuse conv+bn into a single layer to save latency in inference mode
        out = self.relu(out)

        return out


m  = Model(3)

x1 = torch.rand((1, 3, 8, 8))
x2 = m(x1).to('cpu')  # CPU or GPU tensors

