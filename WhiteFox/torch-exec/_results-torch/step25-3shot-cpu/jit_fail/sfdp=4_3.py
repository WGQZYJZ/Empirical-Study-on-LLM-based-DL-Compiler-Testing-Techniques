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


q = torch.randn(2, 5, 1)

k = torch.randn(2, 1, 5)

v = torch.randn(2, 1, 5)


attn_mask = torch.tril(torch.ones((5, 5))).unsqueeze(0).unsqueeze(0).cuda()

test_inputs = [q, k, v, attn_mask]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 1] but got: [2, 5].

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(2, 5, 1)), FakeTensor(..., size=(2, 5, 1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 1] but got: [2, 5].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''