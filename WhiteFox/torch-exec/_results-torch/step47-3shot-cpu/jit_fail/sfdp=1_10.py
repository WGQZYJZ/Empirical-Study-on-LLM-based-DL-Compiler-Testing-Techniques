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

    def forward(self, v1, v2, v3):
        v4 = torch.matmul(v1, v2.transpose(-2, -1))
        v5 = v4.div(v3)
        v6 = torch.softmax(v5, dim=-1)
        v7 = torch.nn.functional.dropout(v6, p=0.5)
        v8 = torch.matmul(v7, v3)
        return v8


func = Model().to('cpu')


v1 = torch.randn(1, 10, 20)

v2 = torch.randn(1, 20, 30)


v3 = torch.arange(1, 20 + 1, dtype=torch.float32)

test_inputs = [v1, v2, v3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 20] but got: [1, 30].

jit:
Failed running call_function <built-in method matmul of type object at 0x7a37ee396ec0>(*(FakeTensor(..., size=(1, 10, 20)), FakeTensor(..., size=(1, 30, 20))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 20] but got: [1, 30].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''