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
        self.conv2d0 = torch.nn.Conv2d(170, 175, 1, stride=1, bias=False)
        self.conv2d1 = torch.nn.Conv2d(175, 3, 10, stride=1, padding=5, bias=False)
        self.conv_t = torch.nn.ConvTranspose2d(8, 5, 1, stride=1, bias=False)

    def forward(self, w1):
        x15 = self.conv2d1(self.conv2d0(w1))
        x16 = (x15 + (- 0.22))
        x17 = (x16 > 0)
        x18 = (x16 * (- 1.05))
        x19 = torch.where(x17, x16, x18)
        x20 = torch.cat((x19, x1), 1)
        x21 = self.conv_t(x20)
        x22 = (x21 + 0.93)
        x23 = (x21 > 0)
        x24 = (x21 * (- 10.89))
        x25 = torch.where(x23, x21, x24)
        return x25




func = Model().to('cuda')



x1 = torch.randn(27, 170, 2, 33)



w1 = torch.randn(5, 8, 43, 9)


test_inputs = [x1, w1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''