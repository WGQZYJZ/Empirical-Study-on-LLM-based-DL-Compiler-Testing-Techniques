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
        self.conv_t = torch.nn.ConvTranspose2d(10, 10, 3, bias=False, padding=(3, 0))

    def forward(self, x4):
        m1 = self.conv_t(x4)
        m2 = (m1 > 0)
        m3 = (m1 * (- 0.30569046525001525))
        m4 = torch.where(m2, m1, m3)
        return torch.nn.functional.conv2d(m4, weight=torch.ones(10, 25, 3, 2), bias=None, stride=(90, 90), padding=None, dilation=1, groups=1)




func = Model().to('cuda')



x4 = torch.randn(27, 10, 88, 22)


test_inputs = [x4]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (Tensor, groups=int, dilation=int, stride=tuple, padding=NoneType, bias=NoneType, weight=Tensor), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (Tensor, weight=Tensor, !bias=NoneType!, !stride=tuple of (int, int)!, !padding=NoneType!, !dilation=int!, groups=int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (Tensor, weight=Tensor, !bias=NoneType!, !stride=tuple of (int, int)!, !padding=NoneType!, !dilation=int!, groups=int)


jit:
Failed running call_function <built-in method conv2d of type object at 0x7555b6a699e0>(*(FakeTensor(..., device='cuda:0', size=(27, 10, 84, 24)),), **{'weight': FakeTensor(..., size=(10, 25, 3, 2)), 'bias': None, 'stride': (90, 90), 'padding': None, 'dilation': 1, 'groups': 1}):
conv2d() received an invalid combination of arguments - got (FakeTensor, groups=int, dilation=int, stride=tuple, padding=NoneType, bias=NoneType, weight=FakeTensor), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !weight=FakeTensor!, !bias=NoneType!, !stride=tuple of (int, int)!, !padding=NoneType!, !dilation=int!, groups=int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !weight=FakeTensor!, !bias=NoneType!, !stride=tuple of (int, int)!, !padding=NoneType!, !dilation=int!, groups=int)


from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''