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
        self.qkv = torch.nn.Linear(3, 6)
        self.attn = torch.nn.Linear(6, 3)

    def forward(self, x):
        v = self.qkv(x)
        (q, k, v) = v.split(split_size, dim=2)
        scale_factor = k.shape[-1] ** 0.5
        q = q * scale_factor
        k = k * scale_factor
        v = v * scale_factor
        attn = self.attn(torch.matmul(q, k.transpose(1, 2)))
        attn = torch.softmax(attn, dim=-1)
        return attn


func = Model().to('cpu')


x = torch.randn(1, 10, 3)

test_inputs = [x]

# JIT_FAIL
'''
direct:
name 'split_size' is not defined

jit:
NameError: name 'split_size' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''