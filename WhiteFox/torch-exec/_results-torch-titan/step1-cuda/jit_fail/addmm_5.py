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
        super(Model, self).__init__()
        self.conv1 = torch.nn.Conv2d(3, 6, kernel_size=3, stride=1, padding=1)
        self.bn = torch.nn.BatchNorm2d(6)
        self.conv2 = torch.nn.Conv2d(6, 8, kernel_size=3, stride=1, padding=1)

    def forward(self, *input):
        x = input
        x1 = self.conv1(x)
        x2 = self.bn(x)
        x3 = (x1 + x2)
        x4 = F.relu(x3)
        x5 = self.conv2(x4)
        x6 = (x5 + x)
        return x6



func = Model().to('cuda')



x = torch.randn(1, 3, 64, 64)


test_inputs = [x]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (tuple, Parameter, Parameter, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!tuple of (Tensor,)!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!tuple of (Tensor,)!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)


jit:
Failed running call_module L__self___conv1(*((FakeTensor(..., device='cuda:0', size=(1, 3, 64, 64)),),), **{}):
conv2d() received an invalid combination of arguments - got (tuple, FakeTensor, FakeTensor, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!tuple of (FakeTensor,)!, !FakeTensor!, !FakeTensor!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!tuple of (FakeTensor,)!, !FakeTensor!, !FakeTensor!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)


from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''