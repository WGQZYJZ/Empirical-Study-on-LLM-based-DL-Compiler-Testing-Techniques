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

    def forward(self, Q, K, V, mask):
        qk = Q @ K.transpose(-2, -1) / math.sqrt(Q.size(-1))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ V
        return output



func = Model().to('cuda')


Q = torch.randn(1, 8, 16, 32)

K = torch.randn(1, 8, 32, 16)

V = torch.randn(1, 8, 32, 16)

mask = torch.randn(8, 16, 32).ge(0).float().fill_(-10000.0)

test_inputs = [Q, K, V, mask]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [8, 32] but got: [8, 16].

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., device='cuda:0', size=(1, 8, s1, s2)), FakeTensor(..., device='cuda:0', size=(1, 8, 16, 32))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [8, s2] but got: [8, 16].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''