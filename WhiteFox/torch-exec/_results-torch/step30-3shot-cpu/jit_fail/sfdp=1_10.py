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
        self.dropout_p = 0.8
        self.dropout = torch.nn.Dropout(self.dropout_p)
        self.dropout.p = 0.8
        self.inv_scale_factor = np.sqrt(1.0 / (1024 * 1024))

    def forward(self, x3, x4):
        v8 = torch.matmul(x3, x4.transpose(-2, -1))
        v9 = v8.div(self.inv_scale_factor)
        v10 = torch.nn.functional.softmax(v9, dim=-1)
        v11 = self.dropout(v10)
        v12 = v11.matmul(x4)
        return v12


func = Model().to('cpu')


x3 = torch.randn(1, 1024, 36)

x4 = torch.randn(1, 64, 1024)

test_inputs = [x3, x4]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 36] but got: [1, 1024].

jit:
Failed running call_function <built-in method matmul of type object at 0x7b0457d96ec0>(*(FakeTensor(..., size=(1, 1024, 36)), FakeTensor(..., size=(1, 1024, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 36] but got: [1, 1024].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''