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

    def forward(self, x1):
        k = torch.randn(1, 9, 24)
        t2 = torch.matmul(x1, k.transpose(0, 1))
        v = torch.randn(24, 24)
        scale = 1.0 / math.sqrt(1)
        t1 = t2.div(scale)
        t3 = torch.softmax(t1)
        t4 = torch.nn.functional.dropout(t3)
        out = torch.matmul(t4, value)
        return out


func = Model().to('cpu')


x1 = torch.randn(24, 9)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [9, 9] but got: [9, 1].

jit:
Failed running call_function <built-in method matmul of type object at 0x7d2885d96ec0>(*(FakeTensor(..., size=(24, 9)), FakeTensor(..., size=(9, 1, 24))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [9, 9] but got: [9, 1].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''