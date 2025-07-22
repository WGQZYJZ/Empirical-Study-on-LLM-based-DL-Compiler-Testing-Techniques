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

class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 7, 5, stride=5, padding=0, dilation=0, groups=3, bias=True)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = 2 + v1
        v3 = v2.clamp(min=0, max=6)
        v4 = v3 / 6
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]
