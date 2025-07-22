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

    def __init__(self, min_value, max_value):
        super().__init__()
        self.linear = torch.nn.Linear(32, 32)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=0.5)
        v3 = torch.clamp_max(v2, max_value=(- 1))
        return v3



min_value = 1
max_value = 1
func = Model(0.5, (- 1)).to('cuda')



x1 = torch.randn(1, 32, 32, 32)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
clamp_min() received an invalid combination of arguments - got (Tensor, min_value=float), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


jit:
Failed running call_function <built-in method clamp_min of type object at 0x7a47a7c699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 32, 32, 32)),), **{'min_value': 0.5}):
clamp_min() received an invalid combination of arguments - got (FakeTensor, min_value=float), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''