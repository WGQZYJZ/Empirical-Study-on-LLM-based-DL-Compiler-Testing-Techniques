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



class Conv_ReL(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.block0 = torch.nn.Sequential(torch.nn.Conv2d(3, 31, (3, 5), bias=False, padding_mode='zeros'), torch.nn.ReLU(inplace=True))

    def forward(self, x1):
        v1 = self.block0(x1)
        v2 = torch.argmax(v1, dim=1)
        v3 = torch.max(v1, dim=1)[1]
        v4 = torch.flatten(torch.mul(v2, v3))
        v5 = torch.nn.functional.pad(v2, (4,), 'constant', 12)
        return torch.transpose(torch.bmm(v4, v5), 0, 1)




func = Conv_ReL().to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (int, Parameter, NoneType, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !NoneType!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !NoneType!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)


jit:
Failed running call_module L__self___block0_0(*(1,), **{}):
conv2d() received an invalid combination of arguments - got (int, FakeTensor, NoneType, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !FakeTensor!, !NoneType!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !FakeTensor!, !NoneType!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)


from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''