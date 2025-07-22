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

    def forward(self, x2, x3):
        v2 = torch.matmul(x2, x3.transpose(-2, -1))
        v3 = v2.mul(2.0)
        v4 = v3.softmax(dim=-1)
        v5 = torch.nn.functional.dropout(v4, p=0.1, training=True)
        v6 = v5.matmul(x3)
        return v6


func = Model().to('cpu')


x2 = torch.randn(3, 4, 5)

x3 = torch.randn(3, 5, 6)

test_inputs = [x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 5] but got: [3, 6].

jit:
Failed running call_function <built-in method matmul of type object at 0x72affc196ec0>(*(FakeTensor(..., size=(3, 4, 5)), FakeTensor(..., size=(3, 6, 5))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [3, 5] but got: [3, 6].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''