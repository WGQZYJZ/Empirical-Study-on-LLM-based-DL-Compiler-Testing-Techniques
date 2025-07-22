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

class Model2(torch.nn.Module):

    def __init__(self):
        super(Model2, self).__init__()

    def forward(self, x1, x2, x4):
        x1 = torch.nn.functional.conv2d(input, weight=x2, bias=x2, stride=x4, padding=x4, dilation=x1, groups=x1)
        return x1



func = Model2().to('cpu')


input = torch.randn(1, 3, 4, 4)

x2 = torch.randn(3, 3, 4, 4)
x1 = 1

test_inputs = [input, x2, x1]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (Tensor, groups=Tensor, dilation=Tensor, stride=int, padding=int, bias=Tensor, weight=Tensor), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, tuple of ints padding = 0, tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: groups, dilation, stride, padding, bias
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, str padding = "valid", tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: groups, dilation, stride, padding, bias


jit:
conv2d() received an invalid combination of arguments - got (Tensor, groups=Tensor, dilation=Tensor, stride=int, padding=int, bias=Tensor, weight=Tensor), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, tuple of ints padding = 0, tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: groups, dilation, stride, padding, bias
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, str padding = "valid", tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: groups, dilation, stride, padding, bias

'''