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
        self.linear = torch.nn.Linear(64, 64)

    def forward(self, q, k, v, mask):
        v1 = self.linear(q).transpose(-2, -1) / math.sqrt(q.size(-1))
        v2 = v1.matmul(k.transpose(-2, -1))
        v3 = v2 + mask
        v4 = torch.softmax(v3, dim=-1)
        return (v4.matmul(v).to(torch.float32),)


func = Model().to('cpu')


q = torch.randn(1, 5, 64)

k = torch.randn(1, 6, 64)

v = torch.randn(1, 6, 64)

mask = torch.ones([1, 5, 6]).eq(0)

test_inputs = [q, k, v, mask]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 5] but got: [1, 64].

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(1, 64, 5)), FakeTensor(..., size=(1, 64, 6))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 5] but got: [1, 64].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''