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
        self.conv = torch.nn.Conv2d(3, 16, 3, stride=2, padding=2, dilation=2, groups=2)
        self.batch_norm = torch.nn.BatchNorm2d(16)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.relu()
        v3 = self.batch_norm(v1)
        v4 = torch.sigmoid(v2 + v3)
        v5 = v3 * v4
        return v5



func = Model().to('cuda')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]
