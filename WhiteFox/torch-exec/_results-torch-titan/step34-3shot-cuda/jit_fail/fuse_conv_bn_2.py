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
        self.conv1 = torch.nn.Conv3d(3, 5, 3)
        self.bn = torch.nn.BatchNorm1d(5)
        self.activation = torch.nn.Sigmoid()

    def forward(self, x1):
        y = self.conv1(x1)
        z = self.bn(y)
        t = self.activation(z)
        return t




func = Model().to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
conv3d() received an invalid combination of arguments - got (int, Parameter, Parameter, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !Parameter!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !Parameter!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, int)


jit:
Failed running call_module L__self___conv1(*(1,), **{}):
conv3d() received an invalid combination of arguments - got (int, FakeTensor, FakeTensor, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !FakeTensor!, !FakeTensor!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !FakeTensor!, !FakeTensor!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, !tuple of (int, int, int)!, int)


from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''