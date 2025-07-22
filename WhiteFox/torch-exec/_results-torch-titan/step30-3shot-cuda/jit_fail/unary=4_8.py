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

    def linear(x1):
        v1 = torch.sum(x1, dim=1, keepdim=True)
        v2 = (v1 * 0.5)
        v3 = (v1 * 0.7071067811865476)
        v4 = torch.erf(v3)
        v5 = (v4 + 1)
        v6 = (v2 * v5)
        return v6

    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 64)

    def forward(self, x2):
        w = self.linear(x2)
        v = self.linear(x2)
        u = self.linear(x2)
        vw = self.linear(vw)
        x3 = self.linear(vw)
        vy = self.linear(vy)
        vz = self.linear(vz)
        wu = self.linear(wu)
        wx = self.linear(wx)
        wy = self.linear(wy)
        wz = self.linear(wz)
        vu = self.linear(vu)
        vx = self.linear(vx)
        vy = self.linear(vy)
        vz = self.linear(vz)
        t1 = (w + v)
        t2 = ((u + vy) + vz)
        t3 = (((vu + vx) + vy) + vz)
        t4 = (((u + vx) + vy) + vz)
        t5 = (((v + wx) + wy) + wz)
        x4 = ((t1 * t2) + t3)
        return x4



func = Model().to('cuda')



x2 = torch.randn(1, 64, 19)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
linear() takes 1 positional argument but 2 were given

jit:
linear() takes 1 positional argument but 2 were given
'''