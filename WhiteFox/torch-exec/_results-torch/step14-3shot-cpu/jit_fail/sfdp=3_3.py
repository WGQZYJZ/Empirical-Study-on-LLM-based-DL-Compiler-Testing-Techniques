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
        self.dropout = torch.nn.Dropout(0.1)

    def forward(self, x1, x2, x3):
        m1 = torch.matmul(x1, x2.transpose(-2, -1))
        v1 = m1 * 1.0
        a1 = torch.nn.functional.softmax(v1, dim=-1)
        d1 = self.dropout(a1)
        v2 = x3 * 1.0
        v3 = d1.matmul(v2)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 12, 30, 20)

x2 = torch.randn(1, 12, 30, 20)

x3 = torch.randn(1, 12, 12, 10)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [12, 30] but got: [12, 12].

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(1, 12, 30, 30)), FakeTensor(..., size=(1, 12, 12, 10))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [12, 30] but got: [12, 12].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''