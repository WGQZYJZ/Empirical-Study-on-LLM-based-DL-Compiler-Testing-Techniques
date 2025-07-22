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

    def forward(self, x1, x2, x2_mask):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1 / math.sqrt(v1.shape[-1])
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.3)
        v5 = torch.matmul(v4, x2)
        return v5


func = Model().to('cpu')


x1 = torch.randn(64, 512, 16)

x2 = torch.randn(64, 16, 1024)

x2_mask = torch.randn(1, 1, 1, 1024)

test_inputs = [x1, x2, x2_mask]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [64, 16] but got: [64, 1024].

jit:
Failed running call_function <built-in method matmul of type object at 0x7d1219f96ec0>(*(FakeTensor(..., size=(64, 512, 16)), FakeTensor(..., size=(64, 1024, 16))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [64, 16] but got: [64, 1024].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''