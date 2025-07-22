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
        self.conv_before = torch.nn.Conv3d(32, 58, kernel_size=(1, 5, 5), stride=(1, 1, 1), bias=False, padding=(0, 0, 0))
        self.conv_after = torch.nn.Conv3d(58, 32, kernel_size=(1, 3, 3), stride=(1, 1, 1), bias=False, padding=(0, 0, 0))

    def forward(self, x2):
        v1 = self.conv_before(x2)
        v2 = v1 - -3.4
        v3 = self.conv_after(v2)
        v4 = v3 + 3.4
        return -v4



func = Model().to('cpu')

x2 = 1

test_inputs = [x2]

# JIT_FAIL
'''
direct:
conv3d() received an invalid combination of arguments - got (int, Parameter, NoneType, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, tuple of ints padding = 0, tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !NoneType!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, !int!)
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, str padding = "valid", tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !NoneType!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, !int!)


jit:
conv3d() received an invalid combination of arguments - got (int, Parameter, NoneType, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, tuple of ints padding = 0, tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !NoneType!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, !int!)
 * (Tensor input, Tensor weight, Tensor bias = None, tuple of ints stride = 1, str padding = "valid", tuple of ints dilation = 1, int groups = 1)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !NoneType!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, !int!)

'''