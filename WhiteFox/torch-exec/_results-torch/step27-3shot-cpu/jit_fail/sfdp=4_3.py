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

    def __init__(self, heads, q_dim, k_dim, v_dim):
        super().__init__()
        self.heads = heads
        self.q_dim = q_dim
        self.k_dim = k_dim
        self.v_dim = v_dim
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, query, key, value, mask=0):
        q = self.conv(query)
        v = self.conv(value)
        k = self.conv(key)
        a = q @ k.transpose(-2, -1) / math.sqrt(self.k_dim) + attn_mask
        attn_weight = torch.softmax(a, dim=-1)
        output = attn_weight @ v
        return output


heads = 1
q_dim = 1
k_dim = 1
v_dim = 1

func = Model(heads, q_dim, k_dim, v_dim).to('cpu')


query = torch.randn(1, 3, 64, 64)

key = torch.randn(1, 3, 128, 128)

value = torch.randn(1, 3, 128, 128)

attn_mask = torch.randn(1, 1, 1, 256)

test_inputs = [query, key, value, attn_mask]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [8, 66] but got: [8, 130].

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(1, 8, 66, 66)), FakeTensor(..., size=(1, 8, 130, 130))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [8, 66] but got: [8, 130].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''