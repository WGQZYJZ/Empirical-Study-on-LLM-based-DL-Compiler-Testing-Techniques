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

    def forward(self, q, k, v, scale_factor, dropout_p):
        qk = torch.matmul(q, k.transpose(-2, -1))
        v_ = v.permute(0, 1, 3, 2)
        qk_ = qk.permute(0, 2, 3, 1)
        qkv = torch.matmul(qk_, v_)
        qkv_ = qkv.permute(0, 3, 1, 2)
        return qkv_


func = Model().to('cpu')


q = torch.randn(2, 3, 8, 8)

k = torch.randn(2, 3, 8, 8)

v = torch.randn(2, 3, 8, 8)
scale_factor = 1
dropout_p = 1

test_inputs = [q, k, v, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x7e9339796ec0>(*(FakeTensor(..., size=(2, 8, 8, 3)), FakeTensor(..., size=(2, 3, 8, 8))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''