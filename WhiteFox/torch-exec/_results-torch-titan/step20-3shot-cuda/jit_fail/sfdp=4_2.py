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
        self.query = torch.nn.Parameter(torch.randn(2, 4, 3))
        self.key = torch.nn.Parameter(torch.randn(6, 4, 5))

    def forward(self, v1):
        qk = ((self.query @ self.key.transpose((- 2), (- 1))) / math.sqrt(self.query.size((- 1))))
        attn_mask = torch.zeros(qk.size(), dtype=torch.bool, device=qk.device)
        attn_mask[:, :, :3, 1:4] = True
        v5 = (qk + attn_mask)
        attn_weight = torch.softmax(qk, dim=(- 1))
        v7 = (attn_weight @ value)
        return v7



func = Model().to('cuda')



x1 = torch.randn(2, 4, 5)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (6) at non-singleton dimension 0

jit:
Failed running call_function <built-in function matmul>(*(Parameter(FakeTensor(..., device='cuda:0', size=(2, 4, 3), requires_grad=True)), FakeTensor(..., device='cuda:0', size=(6, 5, 4), requires_grad=True)), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''