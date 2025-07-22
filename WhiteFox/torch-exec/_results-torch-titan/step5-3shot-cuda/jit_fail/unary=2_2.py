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
        self.gelu = torch.nn.GELU()
        self.conv = torch.nn.Conv2d(10, 10, 3, stride=2, padding=[[3, 5], [4, 6]], dilation=2)
        self.conv_transpose = torch.nn.ConvTranspose2d(10, 10, 3, stride=2, padding=[[7, 9], [10, 12]], dilation=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv_transpose(v1)
        v3 = (v2 - 0.4)
        v4 = self.gelu(v3)
        v5 = (v4 + 0.1)
        return (v4 + v5)




func = Model().to('cuda')



x1 = torch.randn(3, 10, 8, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (Tensor, Parameter, Parameter, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (Tensor, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (list, list)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (Tensor, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (list, list)!, !tuple of (int, int)!, int)


jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(3, 10, 8, 8)),), **{}):
conv2d() received an invalid combination of arguments - got (FakeTensor, FakeTensor, FakeTensor, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !FakeTensor!, !FakeTensor!, !tuple of (int, int)!, !tuple of (list, list)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !FakeTensor!, !FakeTensor!, !tuple of (int, int)!, !tuple of (list, list)!, !tuple of (int, int)!, int)


from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''