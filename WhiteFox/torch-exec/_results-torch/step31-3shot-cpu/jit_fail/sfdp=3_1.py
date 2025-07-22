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
        self.dropout = torch.nn.Dropout(p=0.1)

    def forward(self, q, k, v):
        s = torch.matmul(q, k).mul(0.1)
        a = s.softmax(dim=-1)
        d = self.dropout(a)
        r = torch.matmul(d, v)
        return r


func = Model().to('cpu')


q = torch.randn(1, 120, 1024)

k = torch.randn(1, 120, 1024)

v = torch.randn(1, 120, 512)

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 1024] but got: [1, 120].

jit:
Failed running call_function <built-in method matmul of type object at 0x7ad738996ec0>(*(FakeTensor(..., size=(1, 120, 1024)), FakeTensor(..., size=(1, 120, 1024))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 1024] but got: [1, 120].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''