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
        self.num_heads = 4
        self.dropout_prob = 0.1

    def forward(self, q, v):
        scale_factor = (1 / (self.num_heads ** 0.5))
        q = torch.einsum('bhlk,bhlm->bhlkm', q, q)
        q *= scale_factor
        attn = torch.softmax(q, dim=(- 1))
        attn = torch.nn.functional.dropout(attn, p=0.1)
        return torch.einsum('bhlkm,bkm->bhlk', attn, v)



func = Model().to('cuda')



q = torch.randn(1, 1, 4, 6)



v = torch.randn(1, 4, 6)


test_inputs = [q, v]

# JIT_FAIL
'''
direct:
einsum(): subscript k has size 4 for operand 1 which does not broadcast with previously seen size 6

jit:
Failed running call_function <function einsum at 0x73918f6f0160>(*('bhlkm,bkm->bhlk', FakeTensor(..., device='cuda:0', size=(1, 1, 4, 6, 6)), FakeTensor(..., device='cuda:0', size=(1, 4, 6))), **{}):
einsum(): subscript k has size 4 for operand 1 which does not broadcast with previously seen size 6

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''