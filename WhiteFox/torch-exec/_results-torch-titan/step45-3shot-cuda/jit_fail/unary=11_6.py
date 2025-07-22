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
        v2 = (v1 + 3)
        v3 = torch.clamp_min(v2, 0)
        v4 = torch.clamp_max(v3, 6)
        v5 = (v4 / 6)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 8, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (groups=int, dilation=int, stride=int, padding=int, bias=NoneType, weight=int, input=Tensor, ), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (input=Tensor, !weight=int!, !bias=NoneType!, !stride=int!, !padding=int!, !dilation=int!, groups=int, )
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (input=Tensor, !weight=int!, !bias=NoneType!, !stride=int!, !padding=int!, !dilation=int!, groups=int, )


jit:
Failed running call_function <built-in method conv2d of type object at 0x790cd12699e0>(*(), **{'input': FakeTensor(..., device='cuda:0', size=(1, 8, 64, 64)), 'weight': 0, 'bias': None, 'stride': 1, 'padding': 1, 'dilation': 1, 'groups': 1}):
conv2d() received an invalid combination of arguments - got (groups=int, dilation=int, stride=int, padding=int, bias=NoneType, weight=int, input=FakeTensor, ), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!input=FakeTensor!, !weight=int!, !bias=NoneType!, !stride=int!, !padding=int!, !dilation=int!, groups=int, )
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!input=FakeTensor!, !weight=int!, !bias=NoneType!, !stride=int!, !padding=int!, !dilation=int!, groups=int, )


from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''