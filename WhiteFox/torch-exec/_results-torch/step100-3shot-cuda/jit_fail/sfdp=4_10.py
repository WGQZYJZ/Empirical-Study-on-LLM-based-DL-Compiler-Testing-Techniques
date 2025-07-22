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

    def forward(self, query, key, Va, m4):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + m4
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ Va
        return output



func = Model().to('cuda')


query = torch.randn(1, 64, 56, 56)

key = torch.randn(1, 64, 56, 56)

mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)
Va = 1

test_inputs = [query, key, mask, Va]

# JIT_FAIL
'''
direct:
"baddbmm_cuda" not implemented for 'Bool'

jit:
backend='inductor' raised:
RuntimeError: Only Tensors of floating point and complex dtype can require gradients


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''