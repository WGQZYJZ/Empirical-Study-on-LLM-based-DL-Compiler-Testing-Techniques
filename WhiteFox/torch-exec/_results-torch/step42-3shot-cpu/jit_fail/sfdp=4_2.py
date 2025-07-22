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

    def forward(self, torch_35818239, q, k2, v, mask):
        qk = torch_35818239 @ k2.transpose(-2, -1) / math.sqrt(torch_35818239.size(-1))
        qk = qk + mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v
        return output



func = Model().to('cpu')


Q = torch.randn(1, 64, 56, 56)

K = torch.randn(1, 64, 56, 56)

V = torch.randn(1, 64, 56, 56)

mask = (torch.rand(1, 56, 56) > 0.7).fill_(-1000000000.0)
torch_35818239 = 1

test_inputs = [Q, K, V, mask, torch_35818239]

# JIT_FAIL
'''
direct:
expected m1 and m2 to have the same dtype, but got: float != bool

jit:
backend='inductor' raised:
RuntimeError: Only Tensors of floating point and complex dtype can require gradients


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''