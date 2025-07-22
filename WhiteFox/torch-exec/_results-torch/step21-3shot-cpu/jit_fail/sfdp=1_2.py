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

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.permute(0, 1, 3, 2))
        inv_scale_factor = math.sqrt(x1.shape[-1])
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, 0.1)
        v1 = dropout_qk.matmul(x2)
        return v1


func = Model().to('cpu')


x1 = torch.randn(1, 15, 20, 20)

x2 = torch.randn(1, 20, 1, 100)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
The size of tensor a (15) must match the size of tensor b (20) at non-singleton dimension 1

jit:
Failed running call_function <built-in method matmul of type object at 0x7d4cef196ec0>(*(FakeTensor(..., size=(1, 15, 20, 20)), FakeTensor(..., size=(1, 20, 100, 1))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''