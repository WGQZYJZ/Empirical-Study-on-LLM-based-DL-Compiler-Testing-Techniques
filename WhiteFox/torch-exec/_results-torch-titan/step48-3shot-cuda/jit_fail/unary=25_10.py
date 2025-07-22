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
        self.linear = torch.nn.Linear(1, 1)
        self.negative_slope = 0.1

    def forward(self, x1):
        v0 = self.linear(x1)
        v1 = (v0 > 0)
        v2 = (v0 * self.negative_slope)
        v3 = torch.where(v1, v0)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
where() received an invalid combination of arguments - got (Tensor, Tensor), but expected one of:
 * (Tensor condition)
 * (Tensor condition, Tensor input, Tensor other, *, Tensor out)
 * (Tensor condition, Number self, Tensor other)
 * (Tensor condition, Tensor input, Number other)
 * (Tensor condition, Number self, Number other)


jit:
Failed running call_function <built-in method where of type object at 0x7a67eb6699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 1), dtype=torch.bool), FakeTensor(..., device='cuda:0', size=(1, 1))), **{}):
where() received an invalid combination of arguments - got (FakeTensor, FakeTensor), but expected one of:
 * (Tensor condition)
 * (Tensor condition, Tensor input, Tensor other, *, Tensor out)
 * (Tensor condition, Number self, Tensor other)
 * (Tensor condition, Tensor input, Number other)
 * (Tensor condition, Number self, Number other)


from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''