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
        self.dropout = 0.3

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose(1, 2))
        v2 = v1 * 1.153
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=self.dropout, training=True)
        v5 = torch.matmul(v4, x2)
        return v5


func = Model().to('cpu')


query = torch.randn(8, 192, 256)

key = torch.randn(8, 256, 84)

test_inputs = [query, key]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [8, 256] but got: [8, 84].

jit:
Failed running call_function <built-in method matmul of type object at 0x78b81eb96ec0>(*(FakeTensor(..., size=(s0, s4, s5)), FakeTensor(..., size=(s0, s2, s1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [s0, s5] but got: [s0, s2].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''