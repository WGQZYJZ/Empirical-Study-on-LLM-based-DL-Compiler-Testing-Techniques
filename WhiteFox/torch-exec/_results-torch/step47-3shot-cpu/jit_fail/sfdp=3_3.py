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

    def forward(self, q, k, v, scale_factor, dropout_p):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output


func = Model().to('cpu')


q = torch.randn(2, 5, 3, 4)

k = torch.randn(2, 5, 2, 8)

v = torch.randn(2, 5, 2, 8)

scale_factor = torch.randn(1, 1, 1)
dropout_p = 1

test_inputs = [q, k, v, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [10, 4] but got: [10, 8].

jit:
Failed running call_function <built-in method matmul of type object at 0x7b1ccf996ec0>(*(FakeTensor(..., size=(2, 5, 3, 4)), FakeTensor(..., size=(2, 5, 8, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [10, 4] but got: [10, 8].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''