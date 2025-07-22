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

    def forward(self, x1, x2, x3, x4):
        qk = x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1))
        qk = qk + x3
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ x4
        return output


func = Model().to('cpu')


x1 = torch.randn(2, 6, 16)

x2 = torch.randn(2, 6, 16)

x3 = torch.randn(2, 6, 6, 6)

x4 = torch.randn(2, 6, 16)

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (6) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(2, 6, 6)), FakeTensor(..., size=(2, 6, 6, 6))), **{}):
Attempting to broadcast a dimension of length 6 at -3! Mismatching argument at index 1 had torch.Size([2, 6, 6, 6]); but expected shape should be broadcastable to [1, 2, 6, 6]

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''