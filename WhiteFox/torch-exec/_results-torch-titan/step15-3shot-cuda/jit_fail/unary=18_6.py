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



class model(nn.Module):

    def __init__(self, in_channels, out_channels, kernel_size, stride, padding):
        super(model, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size, stride, padding)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = nn.Sigmoid(v1)
        v3 = self.conv2(v2)
        v4 = nn.Sigmoid(v3)
        return v4




in_channels = 3


out_channels = 16


kernel_size = 1


stride = 1


padding = 1


func = model(in_channels, out_channels, kernel_size, stride, padding).to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
Sigmoid.__init__() takes 1 positional argument but 2 were given

jit:
conv2d() received an invalid combination of arguments - got (Sigmoid, Parameter, Parameter, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!Sigmoid!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!Sigmoid!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)

'''