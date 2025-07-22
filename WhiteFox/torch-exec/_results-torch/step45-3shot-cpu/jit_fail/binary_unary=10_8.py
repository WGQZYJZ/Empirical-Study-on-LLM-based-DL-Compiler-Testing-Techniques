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

    def forward(self, x):
        t1 = F.conv2d(x, 3, 8, 1, stride=1, padding=1, bias=None)
        t2 = t1 + other
        t3 = F.relu(t2)
        return t3



func = Model().to('cpu')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (int, int, int, int, bias=NoneType, padding=int, stride=int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, tuple of ints padding = 0, tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: bias, padding, stride
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, str padding = "valid", tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: bias, padding, stride


jit:
conv2d() received an invalid combination of arguments - got (int, int, int, int, bias=NoneType, padding=int, stride=int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, tuple of ints padding = 0, tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: bias, padding, stride
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, str padding = "valid", tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the keywords were incorrect: bias, padding, stride

'''