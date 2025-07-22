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



class m1(torch.nn.Module):

    def __init__(self, p1, p2):
        super().__init__()
        self.p1 = p1
        self.p2 = p2

    def forward(self, x1):
        x2 = self.p1(x1)
        x3 = self.p2(x2)
        x4 = torch.randint(0, 1, (1,))
        x5 = torch.rand_like(x4)
        x6 = torch.nn.functional.dropout(x3, p=0.2)
        x7 = torch.nn.functional.relu(x6)
        x8 = torch.abs(x7)
        x9 = torch.nn.functional.linear(x8, x5, bias=42)
        x10 = torch.relu(x6)
        return x9




p1 = nn.Linear(2, 4)


p2 = nn.Dropout()


func = m1(p1, p2).to('cuda')



x = torch.randn(1, 2, 2)


test_inputs = [x]

# JIT_FAIL
'''
direct:
"check_uniform_bounds" not implemented for 'Long'

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1, 2, 4)), FakeTensor(..., size=(1,), dtype=torch.int64)), **{'bias': 42}):
linear(): argument 'bias' must be Tensor, not int

from user code:
   File "<string>", line 30, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''