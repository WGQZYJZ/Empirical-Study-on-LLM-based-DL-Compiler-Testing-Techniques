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
        torch.manual_seed(13)
        self.conv1 = torch.nn.Conv2d(1, 1, 1, stride=1, padding=0)
        self.bn = torch.nn.BatchNorm2d(2)
        self.conv2 = torch.nn.Conv2d(2, 2, 2, stride=2, padding=0)

    def forward(self, x2):
        y2 = self.conv1(x2)
        y2 = self.bn(y2[0])
        y2 = torch.nn.functional.batch_norm(y2, self.bn.running_mean, self.bn.running_var, self.bn.weight, self.bn.bias, False, 0.1, 1.0000000002e-07, False)
        output1 = self.conv2(y2)
        return output1




func = Model().to('cuda')

x2 = 1

test_inputs = [x2]

# JIT_FAIL
'''
direct:
conv2d() received an invalid combination of arguments - got (int, Parameter, Parameter, tuple, tuple, tuple, int), but expected one of:
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, tuple of ints padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)
 * (Tensor input, Tensor weight, Tensor bias, tuple of ints stride, str padding, tuple of ints dilation, int groups)
      didn't match because some of the arguments have invalid types: (!int!, !Parameter!, !Parameter!, !tuple of (int, int)!, !tuple of (int, int)!, !tuple of (int, int)!, int)


jit:
Failed running call_module L__self___conv1(*(1,), **{}):
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