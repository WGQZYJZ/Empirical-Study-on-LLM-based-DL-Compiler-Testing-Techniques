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

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1 / 100
        v3 = torch.nn.functional.softmax(v2, dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.3)
        return v4.matmul(x2)


func = Model().to('cpu')


x1 = torch.randn(1, 256, 128)

x2 = torch.randn(1, 128, 256)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 256].

jit:
Failed running call_function <built-in method matmul of type object at 0x7b0457d96ec0>(*(FakeTensor(..., size=(1, 256, 128)), FakeTensor(..., size=(1, 256, 128))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 256].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''