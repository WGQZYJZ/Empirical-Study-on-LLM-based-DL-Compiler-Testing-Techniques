import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3,64,kernel_size=1, 
                                   stride=1, padding=0, bias=False)
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = F.sigmoid(v1)
        v3 = v1 * v2
        return torch.matmul(v3, v3)
m = Model()
# Inputs to the model
x1=torch.randn(1, 3, 64, 64)
