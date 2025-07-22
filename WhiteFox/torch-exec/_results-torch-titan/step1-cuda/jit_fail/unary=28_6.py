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
        self.linear = torch.nn.Linear(8, 8)

    def forward(self, x):
        v2 = torch.nn.functional.relu(self.linear(x))
        v3 = torch.clamp_min(v2, min_value=min_value)
        v1 = torch.clamp_max(v3, max_value=max_value)
        return v1



min_value = 1
max_value = 1

func = Model(min_value, max_value).to('cuda')



x = torch.randn(1, 8)


test_inputs = [x]

# JIT_FAIL
'''
direct:
clamp_min() received an invalid combination of arguments - got (Tensor, min_value=int), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


jit:
Failed running call_function <built-in method clamp_min of type object at 0x732ddf8699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 8)),), **{'min_value': 1}):
clamp_min() received an invalid combination of arguments - got (FakeTensor, min_value=int), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''