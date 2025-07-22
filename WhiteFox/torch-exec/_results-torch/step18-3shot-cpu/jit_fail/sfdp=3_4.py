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
        self.dropout_p = 0.0
        self.scale_factor = 1.0

    def forward(self, q, k, v):
        v1 = torch.matmul(q, k.transpose(-2, -1))
        v2 = v1 * self.scale_factor
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=self.dropout_p)
        v5 = torch.matmul(v4, v)
        return v5


func = Model().to('cpu')


q = torch.randn(1, 16, 25)

k = torch.randn(1, 16, 49)

v = torch.randn(1, 16, 49)

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 25] but got: [1, 49].

jit:
Failed running call_function <built-in method matmul of type object at 0x76937c196ec0>(*(FakeTensor(..., size=(1, 16, 25)), FakeTensor(..., size=(1, 49, 16))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 25] but got: [1, 49].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''