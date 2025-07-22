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
        super(MyModel, self).__init__()
        self.layer1 = torch.nn.Sequential(torch.nn.modules.Conv2d(3, 2, 1, stride=1, padding=1, bias=False))

    def forward(self, x):
        y = self.layer1(x)
        p = torch.nn.functional.max_pool2d(y, (3, 3), stride=(3, 3), padding=(3, 3))
        z = torch.max(y, p)
        return z




class MyModel(torch.nn.Module):

    def __init__(self):
        super(MyModel, self).__init__()
        self.layer1 = torch.nn.Sequential(torch.nn.modules.Conv2d(16, 10, 5, stride=1, padding=1), torch.nn.ReLU(inplace=True), torch.nn.Conv2d(10, 20, 5, stride=1, padding=1), torch.nn.ReLU(inplace=True))

    def forward(self, x):
        x = self.layer1(x)
        y = torch.max(x, 2)
        return y[0]




func = MyModel().to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (int, Parameter, Parameter, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)


jit:
Failed running call_module L__self___layer1_0(*(1,), **{}):
conv2d() received an invalid combination of arguments - got (int, FakeTensor, FakeTensor, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !FakeTensor!, !FakeTensor!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !FakeTensor!, !FakeTensor!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)


from user code:
   File "<string>", line 37, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''