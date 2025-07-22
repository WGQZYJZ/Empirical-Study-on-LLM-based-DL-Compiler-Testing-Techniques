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
        self.conv = torch.nn.Conv2d(46, 50, 3, stride=1, padding=1, dilation=16, groups=46)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.gelu()
        v3 = v1 * v2
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 46, 64, 64)

test_inputs = [x1]
