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

    def forward(self, x1, x2, x3, x4, x5):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk.div(1e-05)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.1)
        output = dropout_qk.matmul(x3)
        return output


func = Model().to('cpu')


x1 = torch.randn(1, 10, 50)

x2 = torch.randn(1, 10, 30)

x3 = torch.randn(1, 10, 1, 1)
x4 = 1
x5 = 1

test_inputs = [x1, x2, x3, x4, x5]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 50] but got: [1, 30].

jit:
Failed running call_function <built-in method matmul of type object at 0x71a34cd96ec0>(*(FakeTensor(..., size=(1, 10, 50)), FakeTensor(..., size=(1, 30, 10))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 50] but got: [1, 30].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''