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
        self.linear = torch.nn.Linear(17, 4)

    def forward(self, x1, x2):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=x2)
        v3 = torch.clamp_max(v2, max_value=0.7071067811865476)
        v4 = v3.sum()
        return v4



min_value = 1
max_value = 1

func = Model(min_value, max_value).to('cuda')



x1 = torch.randn(1, 17)



x2 = torch.randn(1)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
clamp_min() received an invalid combination of arguments - got (Tensor, min_value=Tensor), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


jit:
Failed running call_function <built-in method clamp_min of type object at 0x70174a6699e0>(*(FakeTensor(..., device='cuda:0', size=(1, 4)),), **{'min_value': FakeTensor(..., device='cuda:0', size=(1,))}):
clamp_min() received an invalid combination of arguments - got (FakeTensor, min_value=FakeTensor), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''