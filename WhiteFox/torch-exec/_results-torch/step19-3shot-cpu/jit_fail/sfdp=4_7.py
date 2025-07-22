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

    def forward(self, q, k, v, attn_mask):
        qk = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v
        return output


func = Model().to('cpu')


attn_mask = torch.ones([1, 3, 3]).tril(-1)

q = torch.randn([1, 3, 5, 6])

k = torch.randn([1, 5, 4])

v = torch.randn([1, 5, 6])

test_inputs = [attn_mask, q, k, v]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 3] but got: [3, 6].

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(1, s3, s4)), FakeTensor(..., size=(1, s0, s2, s1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [s0, s4] but got: [s0, s2].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''