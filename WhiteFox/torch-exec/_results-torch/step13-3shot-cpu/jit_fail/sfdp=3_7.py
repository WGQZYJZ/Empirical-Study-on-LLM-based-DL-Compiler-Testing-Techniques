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

    def __init__(self, scale_factor, dropout_p):
        super().__init__()
        self.scale_factor = scale_factor
        self.dropout_p = dropout_p

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1.mul(self.scale_factor)
        v3 = torch.nn.functional.softmax(v2, dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=self.dropout_p)
        return v4.matmul(x2)


scale_factor = 1
dropout_p = 1
func = Model(1e-05, 0.3).to('cpu')


x1 = torch.randn(1, 8, 16)

x2 = torch.randn(1, 8, 24)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 16] but got: [1, 24].

jit:
Failed running call_function <built-in method matmul of type object at 0x764247796ec0>(*(FakeTensor(..., size=(1, 8, 16)), FakeTensor(..., size=(1, 24, 8))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 16] but got: [1, 24].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''