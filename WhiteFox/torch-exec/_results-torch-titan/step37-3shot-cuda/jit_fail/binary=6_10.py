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
        self.linear_1 = torch.nn.Linear(10, 20)
        self.linear_2 = torch.nn.Linear(20, 30)

    def forward(self, hidden):
        t = F.relu(self.linear_1(hidden))
        t1 = self.linear_2(t)
        t2 = t1[:, 1, :, :]
        t3 = (t2 * 0.5)
        t4 = (t2 * 0.7071067811865476)
        t5 = (torch.erf(t4) + 1)
        t6 = ((- t3) * t5)
        return self.linear_2(t6)



func = Model().to('cuda')



x1 = torch.randn(5, 10)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
too many indices for tensor of dimension 2

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., device='cuda:0', size=(5, 30)), (slice(None, None, None), 1, slice(None, None, None), slice(None, None, None))), **{}):
too many indices for tensor of dimension 2

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''