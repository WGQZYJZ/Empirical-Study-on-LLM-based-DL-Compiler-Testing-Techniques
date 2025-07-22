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
        self.conv = torch.nn.Conv2d(640, 160, 16, groups=4)
        self.sigmoid = torch.nn.Sigmoid()
        self.mul = torch.nn.Mul()

    def forward(self, x1):
        v = self.conv(x1)
        v1 = self.sigmoid(v)
        v2 = self.mul(v, v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 640, 64, 64)

test_inputs = [x1]
