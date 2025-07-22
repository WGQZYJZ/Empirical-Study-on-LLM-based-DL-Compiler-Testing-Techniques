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
        self.inv_scale_factor = 10.0
        self.dropout_p = 0.2

    def forward(self, x1, x2, x3):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1.div(self.inv_scale_factor)
        v3 = F.softmax(v2, dim=-1)
        v4 = F.dropout(v3, p=self.dropout_p)
        return torch.matmul(v4, x3)


func = Model().to('cpu')


x1 = torch.randn(1, 5, 200)

x2 = torch.randn(1, 5, 200)

x3 = torch.randn(1, 200, 100)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 5] but got: [1, 200].

jit:
Failed running call_function <built-in method matmul of type object at 0x74f71e996ec0>(*(FakeTensor(..., size=(1, 5, 5)), FakeTensor(..., size=(1, 200, 100))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 5] but got: [1, 200].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''