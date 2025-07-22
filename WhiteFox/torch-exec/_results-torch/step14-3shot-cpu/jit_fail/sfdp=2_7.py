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
        self.scale_factor = 16

    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2.transpose(-2, -1))
        v2 = v1.div(self.scale_factor)
        v3 = v2.softmax(dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.5)
        v5 = torch.matmul(v4, x2)
        return v5


func = Model().to('cpu')


x1 = torch.randn(256, 64, 256)

x3 = torch.randn(256, 32, 64)

test_inputs = [x1, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [256, 256] but got: [256, 64].

jit:
Failed running call_function <built-in method matmul of type object at 0x7a81a4596ec0>(*(FakeTensor(..., size=(256, 64, 256)), FakeTensor(..., size=(256, 64, 32))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [256, 256] but got: [256, 64].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''