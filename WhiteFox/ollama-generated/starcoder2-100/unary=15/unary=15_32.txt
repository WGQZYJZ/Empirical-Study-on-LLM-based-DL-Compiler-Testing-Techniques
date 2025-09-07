

import torch
from torch import nn as nn
class ReluModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1  = self.conv(x) 
        v2  = torch.nn.functional.relu(v1)
        return v2

m  = ReluModel()
