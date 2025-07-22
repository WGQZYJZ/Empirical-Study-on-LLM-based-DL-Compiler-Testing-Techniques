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



class MyModel(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv0 = torch.nn.Conv1d(64, 128, 64, stride=32)
        self.conv1 = torch.nn.Conv1d(128, 128, 50, stride=25)

    def forward(self, x):
        x = torch.relu(self.conv0(x))
        x = torch.tanh(self.conv1(x))
        return torch.max(x)




func = MyModel().to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
conv1d() received an invalid combination of arguments - got (int, Parameter, Parameter, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !Parameter!, !tuple of (int,)!, !tuple of (int,)!, !tuple of (int,)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !Parameter!, !tuple of (int,)!, !tuple of (int,)!, !tuple of (int,)!, int)


jit:
Failed running call_module L__self___conv0(*(1,), **{}):
conv1d() received an invalid combination of arguments - got (int, FakeTensor, FakeTensor, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !FakeTensor!, !FakeTensor!, !tuple of (int,)!, !tuple of (int,)!, !tuple of (int,)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !FakeTensor!, !FakeTensor!, !tuple of (int,)!, !tuple of (int,)!, !tuple of (int,)!, int)


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''