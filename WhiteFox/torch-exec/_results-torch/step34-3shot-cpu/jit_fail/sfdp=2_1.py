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

    def forward(self, q, k, v, scale_factor=1.0, dropout_p=0.0):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk / scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk @ v
        return output


func = Model().to('cpu')


q = torch.randn(1, 8, 16)

k = torch.randn(1, 8, 32)

v = torch.randn(1, 8, 32)

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 16] but got: [1, 32].

jit:
Failed running call_function <built-in method matmul of type object at 0x7ad48e396ec0>(*(FakeTensor(..., size=(1, 8, 16)), FakeTensor(..., size=(1, 32, 8))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 16] but got: [1, 32].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''