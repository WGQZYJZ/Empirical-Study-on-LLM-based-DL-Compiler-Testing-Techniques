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

    def forward(self, q, k, v, attn_mask):
        qk = torch.matmul(q, k.T) / math.sqrt(q.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = torch.matmul(attn_weight, v)
        return output


func = Model().to('cpu')


q = torch.randn(8, 64, 80)

k = torch.randn(8, 24, 80)

v = torch.randn(8, 24, 80)

attn_mask = torch.zeros(8, 80, 80)

test_inputs = [q, k, v, attn_mask]

# JIT_FAIL
'''
direct:
The size of tensor a (8) must match the size of tensor b (80) at non-singleton dimension 0

jit:
Failed running call_function <built-in method matmul of type object at 0x781fa1f96ec0>(*(FakeTensor(..., size=(8, 64, 80)), FakeTensor(..., size=(80, 24, 8))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''