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

    def __init__(self, negative_slope=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope

    def forward(self, x1, m):
        v1 = self.conv(x1)
        v2 = (v1 > 0)
        v3 = (v1 * self.negative_slope)
        v4 = torch.where(m, v1, v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)

m = 1

test_inputs = [x1, m]

# JIT_FAIL
'''
direct:
where() received an invalid combination of arguments - got (int, Tensor, Tensor), but expected one of:
 * (Tensor condition)
 * (Tensor condition, Tensor input, Tensor other, *, Tensor out)
 * (Tensor condition, Number self, Tensor other)
      didn't match because some of the arguments have invalid types: (!int!, !Tensor!, Tensor)
 * (Tensor condition, Tensor input, Number other)
      didn't match because some of the arguments have invalid types: (!int!, Tensor, !Tensor!)
 * (Tensor condition, Number self, Number other)
      didn't match because some of the arguments have invalid types: (!int!, !Tensor!, !Tensor!)


jit:
Failed running call_function <built-in method where of type object at 0x732b0bc699e0>(*(1, FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66)), FakeTensor(..., device='cuda:0', size=(1, 8, 66, 66))), **{}):
where() received an invalid combination of arguments - got (int, FakeTensor, FakeTensor), but expected one of:
 * (Tensor condition)
 * (Tensor condition, Tensor input, Tensor other, *, Tensor out)
 * (Tensor condition, Number self, Tensor other)
      didn't match because some of the arguments have invalid types: (!int!, !FakeTensor!, !FakeTensor!)
 * (Tensor condition, Tensor input, Number other)
      didn't match because some of the arguments have invalid types: (!int!, !FakeTensor!, !FakeTensor!)
 * (Tensor condition, Number self, Number other)
      didn't match because some of the arguments have invalid types: (!int!, !FakeTensor!, !FakeTensor!)


from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''