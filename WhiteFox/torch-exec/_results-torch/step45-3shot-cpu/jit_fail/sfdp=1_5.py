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

    def forward(self, x, y):
        v1 = torch.matmul(x, y.transpose(-2, -1))
        v2 = v1.div(0.125)
        v3 = v2.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(v3, p=0.1)
        output = torch.matmul(dropout_qk, y)
        return output


func = Model().to('cpu')


x = torch.randn(1, 16, 128)

y = torch.randn(1, 128, 2)

test_inputs = [x, y]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 2].

jit:
Failed running call_function <built-in method matmul of type object at 0x71e256d96ec0>(*(FakeTensor(..., size=(1, 16, 128)), FakeTensor(..., size=(1, 2, 128))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 2].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''