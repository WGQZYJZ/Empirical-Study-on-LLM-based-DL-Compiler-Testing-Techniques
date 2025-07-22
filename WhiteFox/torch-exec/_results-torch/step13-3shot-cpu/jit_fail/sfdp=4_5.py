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
        self.query = torch.nn.Parameter(torch.randn(16, 10, 3072))
        self.key = torch.nn.Parameter(torch.randn(16, 10, 3072))
        self.value = torch.nn.Parameter(torch.randn(16, 12, 3072))
        self.attn_mask = torch.nn.Parameter(torch.tril(torch.ones(16, 10, 10)).view(16, 10, 10), requires_grad=False)

    def forward(self, x2):
        q = self.query[:x2.size(0), :, :].view(x2.size(0), x2.size(1), -1)
        k = self.key[:x2.size(0), :, :].transpose(-2, -1)
        v = self.value[:x2.size(0), :, :].transpose(-2, -1)
        qk = q @ k / math.sqrt(q.size(-1))
        qk = qk + self.attn_mask.unsqueeze(1).repeat(1, x2.size(1), 1, 1)
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v
        return output


func = Model().to('cpu')


x2 = torch.randn(16, 10, 3072)

test_inputs = [x2]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (10) at non-singleton dimension 1

jit:
Failed running call_function <built-in function add>(*(FakeTensor(..., size=(16, 10, 10)), FakeTensor(..., size=(16, 10, 10, 10))), **{}):
Attempting to broadcast a dimension of length 10 at -3! Mismatching argument at index 1 had torch.Size([16, 10, 10, 10]); but expected shape should be broadcastable to [1, 16, 10, 10]

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''