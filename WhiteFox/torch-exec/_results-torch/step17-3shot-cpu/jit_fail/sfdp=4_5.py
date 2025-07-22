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
        self.attn_mask = torch.tensor([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]])

    def forward(self, x1, x2):
        qk = x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1))
        qk = qk + self.attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ x2
        return output


func = Model().to('cpu')


x1 = torch.randn(1, 2, 3, 4)

x2 = torch.randn(1, 4, 5, 6)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (2) must match the size of tensor b (4) at non-singleton dimension 1

jit:
Failed running call_function <built-in function matmul>(*(FakeTensor(..., size=(1, s0, s1, s2)), FakeTensor(..., size=(1, 4, 6, 5))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''