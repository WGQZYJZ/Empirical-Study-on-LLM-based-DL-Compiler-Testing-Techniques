import torch
from torch import nn
 
class Model(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv  = nn.Conv2d(3, 8, kernel_size=1)
        # self.conv.weight.data = self.conv.weight.data * 0.5
 
        self.clamp_min  = torch.nn.functional.relu6

    def forward(self, x):
        conv = self.conv(x)

        t3  = self.clamp_min(conv)
m = Model()
 x1  = torch.randn(4, 3, 64, 64)
