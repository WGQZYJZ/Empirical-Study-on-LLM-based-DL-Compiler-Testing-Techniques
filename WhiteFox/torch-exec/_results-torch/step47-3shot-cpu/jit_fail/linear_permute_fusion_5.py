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
        self.linear = torch.nn.Linear(2, 6)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias)
        v2 = v1.permute(0, 1, 3, 2)
        v3 = v2.permute(0, 2, 3, 1)
        v4 = v1 + v3
        v5 = v4 + v3
        v6 = v5 + v3
        v7 = v6 + v3
        v8 = v6 + v3
        v9 = v1.permute(0, 3, 1, 2)
        v10 = v3 + v9
        v11 = v10 + v1
        v12 = v11 + v10
        v13 = v12 + v10
        v14 = v13 + v10
        v15 = v10.permute(0, 1, 3, 2)
        v16 = v8 + v15
        v17 = v16.permute(0, 2, 1, 3)
        v18 = v17 + v17.permute(0, 2, 3, 1)
        return v17



func = Model().to('cpu')


x1 = torch.randn(2, 6, 2, 2)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (6) must match the size of tensor b (2) at non-singleton dimension 3

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(s0, 6, s2, 6)), FakeTensor(..., size=(s0, 6, 6, s2))), **{}):
The size of tensor a (6) must match the size of tensor b (s2) at non-singleton dimension 3)

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''