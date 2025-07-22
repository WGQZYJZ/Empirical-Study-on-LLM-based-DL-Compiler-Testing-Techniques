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
        x2 = torch.nn.functional.gelu(x1, approximate=False)
        x3 = x2.t().contiguous()
        o1 = x3[0, :]
        o2 = F.softmax(o1, dim=0)
        o3 = F.dropout(o2, p=0.5277)
        return o3




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
gelu(): argument 'approximate' must be str, not bool

jit:
Failed running call_function <built-in function gelu>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2)),), **{'approximate': False}):
gelu(): argument 'approximate' must be str, not bool

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''