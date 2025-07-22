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
        self.linear1 = torch.nn.Linear(17, 2048)
        self.linear2 = torch.nn.Linear(2048, 2048, bias=False)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear1.weight)
        v2 = v1.permute(0, 2, 1)
        v3 = torch.tanh(v2)
        v4 = v3.permute(0, 2, 1).contiguous()
        v5 = torch.tanh(v4)
        v6 = v5.permute(2, 0, 1)
        v7 = torch.nn.functional.linear(v6, self.linear2.weight)
        return v7




func = Model().to('cuda')



x1 = torch.randn(((1 << 10) + 1), 17, 1)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (17425x1 and 17x2048)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., device='cuda:0', size=(1025, 17, 1)), Parameter(FakeTensor(..., device='cuda:0', size=(2048, 17), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [17425, 1] X [17, 2048].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''