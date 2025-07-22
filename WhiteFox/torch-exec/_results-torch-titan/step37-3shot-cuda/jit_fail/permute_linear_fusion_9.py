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
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        x2 = torch.nn.functional.relu(v2)
        v3 = torch.nn.functional.gelu(v2)
        x3 = (v3 + 0.5).floor().to(torch.int64)
        v4 = torch.nn.functional.softmax(x3, (- 1))
        v4 = torch.max(v4, dim=(- 1)).values
        x4 = v4.unsqueeze(dim=1)
        v3 = torch.mul(v1, x4)
        x5 = v3.floor().to(torch.int64)
        x5 = torch.clamp(x5, 0, 1)
        x6 = v3.floor().to(torch.int64)
        x6 = torch.clamp(x6, (- 1), 0)
        v5 = (x5 - x6)
        v6 = (v5 * 2)
        v7 = torch.nn.functional.softmax(v6, (- 1))
        v8 = v7.unsqueeze(dim=1)
        return torch.nn.functional.linear(v5, v8)




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
"host_softmax" not implemented for 'Long'

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 2), dtype=torch.int64), FakeTensor(..., device='cuda:0', size=(1, 1, 2, 2), dtype=torch.int64)), **{}):
t() expects a tensor with <= 2 dimensions, but self is 4D

from user code:
   File "<string>", line 39, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''