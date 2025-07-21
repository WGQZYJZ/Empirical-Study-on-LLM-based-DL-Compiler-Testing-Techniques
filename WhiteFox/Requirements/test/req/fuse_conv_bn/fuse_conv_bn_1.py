import torch
import torch.nn as nn

class ExampleModel(nn.Module):
    def __init__(self):
        super(ExampleModel, self).__init__()
        self.conv = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3)
        self.bn = nn.BatchNorm2d(16)
    
    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return x

model = ExampleModel()
