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

    def __init__(self, n_head, d_qkv):
        super().__init__()
        self.n_head = n_head
        self.d_head = d = d_qkv // n_head

    def forward(self, query, key, value, attn_mask=None):
        n_state = key.size()
        bsz = key.size(1)
        n_head = self.n_head
        d_head = self.d_head
        v1 = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(n_state)
        v2 = v1 + (attn_mask.unsqueeze(-3) if attn_mask is not None else 0)
        attn_weight = attn_weight = torch.softmax(v2.contiguous().view(-1, bsz * n_head, n_state).transpose(0, 1), 1)
        output = torch.matmul(attn_weight.view(bsz * n_head, -1, n_state), value)
        return output.view(bsz, n_head, d_head)


n_head = 1
d_qkv = 1
func = Model(8, 256).to('cpu')


x1 = torch.rand(1, 3, 64, 64)

x2 = torch.rand(1, 3, 64, 64)

x3 = torch.rand(1, 3, 64, 64)
query = 1

test_inputs = [x1, x2, x3, query]

# JIT_FAIL
'''
direct:
must be real number, not torch.Size

jit:
TypeError: must be real number, not torch.Size

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''