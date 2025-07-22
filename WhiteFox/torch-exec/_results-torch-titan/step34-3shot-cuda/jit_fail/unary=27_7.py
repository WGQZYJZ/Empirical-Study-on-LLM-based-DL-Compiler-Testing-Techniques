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

    def __init__(self, min, max):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 11, kernel_size=(2,), stride=(2,), padding=((2,),))
        self.min = min
        self.max = max

    def forward(self, input_tensor=torch.zeros(1, 3, 10, 10)):
        t1 = self.conv(input_tensor)
        t2 = torch.clamp(t1, self.min, self.max)
        t3 = torch.relu(t2)
        return t3




min = 1.1


max = (- 0.9)


func = Model(min, max).to('cuda')



x1 = torch.randn(1, 3, 100, 100)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (Tensor, Parameter, Parameter, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (Tensor, !Parameter!, !Parameter!, !tuple of (int,)!, !tuple of (tuple,)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (Tensor, !Parameter!, !Parameter!, !tuple of (int,)!, !tuple of (tuple,)!, !tuple of (int, int)!, int)


jit:
Failed running call_module L__self___conv(*(FakeTensor(..., device='cuda:0', size=(1, 3, 100, 100)),), **{}):
conv2d() received an invalid combination of arguments - got (FakeTensor, FakeTensor, FakeTensor, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !FakeTensor!, !FakeTensor!, !tuple of (int,)!, !tuple of (tuple,)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!FakeTensor!, !FakeTensor!, !FakeTensor!, !tuple of (int,)!, !tuple of (tuple,)!, !tuple of (int, int)!, int)


from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''