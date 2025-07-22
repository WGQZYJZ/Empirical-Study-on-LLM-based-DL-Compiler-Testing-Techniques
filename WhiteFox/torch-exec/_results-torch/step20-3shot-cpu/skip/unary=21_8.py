import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg

class model_relu(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(1, 4, kernel_size=5, stride=3, padding=0)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = F.relu(v1)
    return v2



func = model_relu().to('cpu')


x = torch.randn(2, 1, 288, 288)

test_inputs = [x]
