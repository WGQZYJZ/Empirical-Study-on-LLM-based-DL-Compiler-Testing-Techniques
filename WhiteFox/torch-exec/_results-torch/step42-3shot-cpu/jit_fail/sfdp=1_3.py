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
        self.query = torch.nn.Linear(32, 8, bias=False)
        self.key = torch.nn.Conv1d(768, 32, 1)

    def forward(self, x1, x2):
        v1 = self.query(x1)
        v2 = self.key(x2)
        v3 = torch.matmul(v1, v2.transpose(-2, -1))
        v4 = v3.div(0.0625)
        v5 = torch.nn.functional.softmax(v4, dim=-1)
        v6 = torch.nn.functional.dropout(v5, p=0.2)
        output = v5.matmul(x2)
        return output


func = Model().to('cpu')


x1 = torch.randn(2, 32)

x2 = torch.randn(16, 768, 128)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [16, 8] but got: [16, 128].

jit:
Failed running call_function <built-in method matmul of type object at 0x7d1219f96ec0>(*(FakeTensor(..., size=(2, 8)), FakeTensor(..., size=(16, 128, 32))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [16, 8] but got: [16, 128].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''