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

    def masked_attention(self, q, k, v, attn_mask):
        q_k = torch.matmul(q, k)
        q_k = torch.div(q_k, math.sqrt(q.shape[-1]))
        q_k = q_k + attn_mask
        q_k = torch.softmax(q_k, dim=-1)
        return torch.matmul(q_k, v)

    def forward(self, q, k, v, attn_mask):
        v_ = self.masked_attention(q, k, v, attn_mask)
        return v_


func = Model().to('cpu')


q = torch.randn(4, 8, 32)

k = torch.randn(4, 24, 32)

v = torch.randn(4, 24, 32)

attn_mask = torch.randn(4, 32)

test_inputs = [q, k, v, attn_mask]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [4, 32] but got: [4, 24].

jit:
Failed running call_function <built-in method matmul of type object at 0x7168b3596ec0>(*(FakeTensor(..., size=(4, 8, 32)), FakeTensor(..., size=(4, 24, 32))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [4, 32] but got: [4, 24].

from user code:
   File "<string>", line 26, in forward
  File "<string>", line 19, in masked_attention


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''