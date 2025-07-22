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
        self.a3 = torch.nn.Conv2d(3, 32, 3, stride=2, padding=0)
        self.a4 = torch.nn.Conv2d(32, 64, 3, stride=2, padding=1)
        self.a5 = torch.nn.Conv2d(64, 128, 3, stride=2, padding=1)
        self.a6 = torch.nn.Conv2d(128, 256, 3, stride=2, padding=1)

    def forward(self, x1, x2, x3, x4, x5):
        x1 = self.a3(x1)
        x2 = self.a4(x2)
        x3 = self.a5(x3)
        x4 = self.a6(x4)
        x6 = torch.cat([x1, x2], 1)
        x7 = torch.cat([x6, x3], 1)
        x8 = torch.cat([x7, x4], 1)
        x9 = torch.cat([x8, x5], 1)
        x10 = (x9 + x5)
        return x10




func = Model().to('cuda')

x1 = 1
x2 = 1
x3 = 1
x4 = 1
x5 = 1

test_inputs = [x1, x2, x3, x4, x5]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (int, Parameter, Parameter, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)


jit:
Failed running call_module L__self___a3(*(1,), **{}):
conv2d() received an invalid combination of arguments - got (int, FakeTensor, FakeTensor, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !FakeTensor!, !FakeTensor!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !FakeTensor!, !FakeTensor!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)


from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''