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

    def forward(self, x1, x2, x3):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x1, x2)
        v3 = torch.mm(x1, x2)
        t1 = v1 * v2 * v3
        v4 = torch.mm(x1, x2)
        v5 = torch.mm(x1, x2)
        v6 = torch.mm(x1, x2)
        t2 = v4 * v5 * v6
        v7 = torch.mm(x1, x2)
        v8 = torch.mm(x1, x2)
        v9 = torch.mm(x1, x2)
        t3 = v7 * v8 * v9
        v10 = torch.mm(x1, x2)
        v11 = torch.mm(x1, x2)
        v12 = torch.mm(x1, x2)
        t4 = v10 * v11 * v12
        t5 = torch.cat([t1, t2], 1)
        t6 = torch.cat([t3, t4], 1)
        return v1 * t5 * v1 * t6



func = Model().to('cuda')


x1 = torch.randn(4, 3)

x2 = torch.randn(3, 2)

x3 = torch.randn(2, 2)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in function mul>(*(FakeTensor(..., device='cuda:0', size=(4, 2)), FakeTensor(..., device='cuda:0', size=(4, 4))), **{}):
Attempting to broadcast a dimension of length 4 at -1! Mismatching argument at index 1 had torch.Size([4, 4]); but expected shape should be broadcastable to [4, 2]

from user code:
   File "<string>", line 37, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''