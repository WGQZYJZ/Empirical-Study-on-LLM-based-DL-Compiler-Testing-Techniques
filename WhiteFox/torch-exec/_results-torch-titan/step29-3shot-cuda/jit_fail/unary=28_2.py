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
        self.linear = torch.nn.Linear(in_features=5, out_features=7, bias=True)

    def forward(self, x2):
        o1 = self.linear(x2)
        o2 = torch.clamp_min(o1, min_value=0.1217971)
        o3 = torch.clamp_max(o2, max_value=1.202422)
        return o3



func = Model().to('cuda')



x2 = torch.randn(4, 5)


test_inputs = [x2]

# JIT_FAIL
'''
direct:
clamp_min() received an invalid combination of arguments - got (Tensor, min_value=float), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


jit:
Failed running call_function <built-in method clamp_min of type object at 0x7d5723e699e0>(*(FakeTensor(..., device='cuda:0', size=(4, 7)),), **{'min_value': 0.1217971}):
clamp_min() received an invalid combination of arguments - got (FakeTensor, min_value=float), but expected one of:
 * (Tensor input, Tensor min, *, Tensor out)
 * (Tensor input, Number min, *, Tensor out)


from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''