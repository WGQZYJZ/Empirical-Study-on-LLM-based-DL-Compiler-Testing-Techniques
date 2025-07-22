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

    def forward(self, key, value, query, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ value
        return output


func = Model().to('cuda')


key = torch.randn(4, 1, 2, 3)

value = torch.randn(4, 5, 2, 3)

query = torch.randn(4, 6, 2, 3)

attn_mask = torch.randn(4, 6, 6, 1)

test_inputs = [key, value, query, attn_mask]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (6) at non-singleton dimension 2

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., device='cuda:0', size=(s0, s4, s5, s1)), FakeTensor(..., device='cuda:0', size=(s7, s8, s9, 1))), **{}):
The size of tensor a (s5) must match the size of tensor b (s9) at non-singleton dimension 2)

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''