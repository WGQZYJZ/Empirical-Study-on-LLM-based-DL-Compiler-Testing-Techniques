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
        self.linear = torch.nn.Linear(10, 20)

    def forward(self, x1):
        v1 = self.linear(x1)
        tmp0 = 0.1
        v3 = (tmp0 > 0)
        v4 = v1[v3]
        v5 = (v1 * tmp0)
        v6 = torch.where(v3, v1, v5)
        return v6



func = Model().to('cuda')



x1 = torch.randn(123, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
where() received an invalid combination of arguments - got (bool, Tensor, Tensor), but expected one of:
 * (Tensor condition)
 * (Tensor condition, Tensor input, Tensor other, *, Tensor out)
 * (Tensor condition, Number self, Tensor other)
      didn't match because some of the arguments have invalid types: (!bool!, !Tensor!, Tensor)
 * (Tensor condition, Tensor input, Number other)
      didn't match because some of the arguments have invalid types: (!bool!, Tensor, !Tensor!)
 * (Tensor condition, Number self, Number other)
      didn't match because some of the arguments have invalid types: (!bool!, !Tensor!, !Tensor!)


jit:
Failed running call_function <built-in method where of type object at 0x7902242699e0>(*(True, FakeTensor(..., device='cuda:0', size=(123, 20)), FakeTensor(..., device='cuda:0', size=(123, 20))), **{}):
where() received an invalid combination of arguments - got (bool, FakeTensor, FakeTensor), but expected one of:
 * (Tensor condition)
 * (Tensor condition, Tensor input, Tensor other, *, Tensor out)
 * (Tensor condition, Number self, Tensor other)
      didn't match because some of the arguments have invalid types: (!bool!, !FakeTensor!, !FakeTensor!)
 * (Tensor condition, Tensor input, Number other)
      didn't match because some of the arguments have invalid types: (!bool!, !FakeTensor!, !FakeTensor!)
 * (Tensor condition, Number self, Number other)
      didn't match because some of the arguments have invalid types: (!bool!, !FakeTensor!, !FakeTensor!)


from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''