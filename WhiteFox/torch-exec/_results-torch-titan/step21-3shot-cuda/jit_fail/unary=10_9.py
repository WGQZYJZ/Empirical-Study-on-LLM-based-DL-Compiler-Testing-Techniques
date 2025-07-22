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

    def forward(self, x1):
        b1 = torch.flatten(x1)
        d1 = b1[(..., np.newaxis)]
        l1 = torch.nn.functional.linear(d1, 2, bias=None)
        l2 = (l1 + 3)
        l3 = torch.clamp_min(l2, 0)
        l4 = torch.clamp_max(l3, 6)
        l5 = (l4 / 6)
        return l5



func = Model().to('cuda')



x1 = torch.randn(1, 100, 100)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
linear(): argument 'weight' (position 2) must be Tensor, not int

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(10000, 1)), 2), **{'bias': None}):
linear(): argument 'weight' (position 2) must be Tensor, not int

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''