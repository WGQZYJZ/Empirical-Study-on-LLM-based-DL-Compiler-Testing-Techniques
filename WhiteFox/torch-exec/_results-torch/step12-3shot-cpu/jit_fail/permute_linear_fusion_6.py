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
        self.linear0 = torch.nn.Linear(2, 2, bias=False)
        self.linear1 = torch.nn.Linear(2, 2, bias=False)
        self.linear2 = torch.nn.Linear(2, 2, bias=False)

    def forward(self, x1):
        v1 = torch.nn.functional.pad(x1, (0, 1), 'constant', 0)
        v2 = torch.nn.functional.pad(6 - x1, (1, 0), 'constant', 0)
        v3 = v1 + v1 + v2 + v2
        v4 = x1.unsqueeze(dim=-1)
        v5 = torch.cat([v4, v4, v4, v4], dim=-1)
        v6 = v1.unsqueeze(dim=-1)
        v7 = torch.cat([v6, v6, v6, v6], dim=-1)
        v8 = v2.unsqueeze(dim=-1)
        v9 = torch.cat([v8, v8, v8, v8], dim=-1)
        v5 = torch.nn.functional.linear(v5, self.linear0.weight)
        v7 = torch.nn.functional.linear(v7, self.linear1.weight)
        v9 = torch.nn.functional.linear(v9, self.linear2.weight)
        v10 = torch.mul(v5, v7)
        v11 = v1 + v3
        v12 = v9 * v7
        v13 = v10 + v11 + v12
        v14 = v3 - v13
        v15 = v3 * 5
        v16 = v14 * v15
        v17 = torch.nn.functional.linear(v16, self.linear0.weight)
        v18 = v15 * v15
        v19 = torch.nn.functional.linear(v18, self.linear1.weight)
        v20 = v18 * v15
        v21 = torch.nn.functional.linear(v20, self.linear2.weight)
        v21 = v15 * v13
        v21 = torch.add(v17, v21, alpha=-1)
        v22 = v1 * v19
        v23 = v4 + v5
        v23 = torch.cat([v23, v23, v23, v23], dim=-1)
        v24 = v9 + v7
        v24 = torch.cat([v24, v24, v24, v24], dim=-1)
        v22 = v22 + v2 + v24
        v23 = torch.nn.functional.linear(v23, self.linear0.weight)
        v25 = v21 * v24
        v23 = v23 + v25
        v24 = 1.0 * 2.0
        v26 = v24 * v21
        v23 = torch.mul(v23, v26)
        v23 = v22.to(torch.bfloat16)
        return v23



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (4x4 and 2x2)

jit:
Failed running call_function <built-in function linear>(*(FakeTensor(..., size=(1, 2, 2, 4)), Parameter(FakeTensor(..., size=(2, 2), requires_grad=True))), **{}):
a and b must have same reduction dim, but got [4, 4] X [2, 2].

from user code:
   File "<string>", line 31, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''