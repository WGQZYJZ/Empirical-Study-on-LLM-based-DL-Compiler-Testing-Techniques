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
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 16, 3)

    def forward(self, x1):
        t0 = torch.conv2d(input=x1, weight=0, bias=None, stride=1, padding=1, dilation=1, groups=1)
        v1 = self.conv_transpose(t0)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = v4 / 6
        return v5



func = Model().to('cpu')


x1 = torch.randn(1, 8, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (groups=int, dilation=int, stride=int, padding=int, bias=NoneType, weight=int, input=Tensor, ), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, tuple of ints padding = 0, tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: groups, dilation, stride, padding, bias
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, str padding = "valid", tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: groups, dilation, stride, padding, bias


jit:
conv2d() received an invalid combination of arguments - got (groups=int, dilation=int, stride=int, padding=int, bias=NoneType, weight=int, input=Tensor, ), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, tuple of ints padding = 0, tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: groups, dilation, stride, padding, bias
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, str padding = "valid", tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: groups, dilation, stride, padding, bias

'''