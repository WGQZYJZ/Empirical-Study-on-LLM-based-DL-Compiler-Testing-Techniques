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

    def forward(self, q, k, v3, mask):
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        qk = qk + mask
        attn_weight_1 = torch.softmax(qk, dim=-1)
        output_1 = attn_weight_1 @ v3.unsqueeze(-2) * attn_weight_1.unsqueeze(1).unsqueeze(-1)
        output_1 = torch.sum(output_1, dim=2)
        output = output_1.squeeze(-1)
        return output



func = Model().to('cpu')


Q = torch.randn(1, 64, 56, 56)

K = torch.randn(1, 64, 56, 56)

V = torch.randn(1, 64, 56, 56)

mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)

test_inputs = [Q, K, V, mask]

# JIT_FAIL
'''
direct:
The size of tensor a (64) must match the size of tensor b (56) at non-singleton dimension 2

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(1, 64, 56, 56)), FakeTensor(..., size=(1, 64, 56, 1, 56))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''