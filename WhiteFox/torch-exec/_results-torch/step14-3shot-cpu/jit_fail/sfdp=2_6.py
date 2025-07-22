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

    def forward(self, x1, x2, x3):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        softmax_qk = qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)
        output = dropout_qk.matmul(x3)


func = Model().to('cpu')


x1 = torch.randn(1, 32, 63)

x2 = torch.randn(1, 64, 32)

x3 = torch.randn(32, 32)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 63] but got: [1, 32].

jit:
Failed running call_function <built-in method matmul of type object at 0x7a81a4596ec0>(*(FakeTensor(..., size=(1, 32, 63)), FakeTensor(..., size=(1, 32, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 63] but got: [1, 32].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''