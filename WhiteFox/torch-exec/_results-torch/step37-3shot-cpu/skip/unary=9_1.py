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
        self.conv = torch.nn.Conv2d(3, 8, 9, padding=1, groups=5)

    def forward(self, x1):
        v1 = 3 + self.conv(x1)
        v2 = v1.clamp(min=0, max=6)
        v3 = v2.div(6)
        v4 = v1 - 3
        v5 = v4.clamp(min=0, max=6)
        v6 = v5.div(6)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]
