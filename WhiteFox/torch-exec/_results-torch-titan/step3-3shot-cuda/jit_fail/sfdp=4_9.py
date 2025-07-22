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

    def forward(self, input, attn_mask):
        attn_mask = torch.zeros(attn_mask.size()).masked_fill_(attn_mask, (- float('inf')))
        attn_mask = torch.transpose(attn_mask, 0, 1)
        v = (input @ input.transpose(1, 2))
        mask = ((1.0 - attn_mask) * (- 10000.0))
        v = (v + mask)
        w = torch.empty_like(v).uniform_((- 0.1), 0.1)
        w = torch.softmax(w, dim=(- 1))
        for i in range(w.shape[(- 1)]):
            w[:, i] = (w[:, i] / torch.norm(w[:, i], 1))
        return (w @ input)



func = Model().to('cuda')



input = torch.randn(20, 30, 10)



attn_mask = torch.zeros(20, 10)


test_inputs = [input, attn_mask]

# JIT_FAIL
'''
direct:
expected self and mask to be on the same device, but got mask on cuda:0 and self on cpu

jit:
Failed running call_method masked_fill_(*(FakeTensor(..., size=(20, 10)), FakeTensor(..., device='cuda:0', size=(20, 10)), -inf), **{}):
Unhandled FakeTensor Device Propagation for aten.masked_fill_.Scalar, found two different devices cpu, cuda:0

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''