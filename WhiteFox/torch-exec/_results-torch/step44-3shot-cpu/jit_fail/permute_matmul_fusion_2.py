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

    def forward(self, x0, x1):
        v0 = x0.unsqueeze(1)
        v1 = x0.unsqueeze(1)
        v2 = x1.unsqueeze(0)
        v3 = x1.unsqueeze(0)
        v4 = x0.view(10, 1, 2, 2)
        v5 = x0.view(10, 1, 2, 2)
        v6 = x1.view(1, 2, 2)
        v7 = v6.unsqueeze(1)
        v8 = v6.unsqueeze(0)
        v9 = x1.permute(2, 0, 1)
        v10 = x0.permute(0, 2, 1)
        v11 = torch.bmm(v10, v9)
        v12 = v0.squeeze(1)
        v13 = torch.bmm(v12, v0)
        v14 = torch.bmm(v12, v1)
        v15 = v2.squeeze(0)
        v16 = torch.bmm(v5, v15)
        v17 = torch.bmm(v4, v11)
        v18 = torch.bmm(v5, v9)
        v19 = torch.bmm(v5, v8)
        v20 = v5.squeeze(1)
        v21 = torch.bmm(v10, v1)
        v22 = v2.permute(2, 0, 1)
        v23 = torch.matmul(v1, v4)
        v24 = torch.bmm(v3, v24)
        return x1



func = Model().to('cpu')


x0 = torch.randn(2, 2)

x1 = torch.randn(3, 3)

test_inputs = [x0, x1]

# JIT_FAIL
'''
direct:
shape '[10, 1, 2, 2]' is invalid for input of size 4

jit:
Failed running call_method view(*(FakeTensor(..., size=(s0, s1)), 10, 1, 2, 2), **{}):
shape '[10, 1, 2, 2]' is invalid for input of size s0*s1

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''