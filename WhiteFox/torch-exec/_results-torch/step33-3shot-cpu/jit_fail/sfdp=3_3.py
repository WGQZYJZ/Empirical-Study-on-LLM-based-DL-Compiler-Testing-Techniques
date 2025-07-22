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

    def forward(self, q, k, v, dropout_p):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scale_factor = qk.shape[-1]
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return (q, k, v, dropout_p, output)


func = Model().to('cpu')


q = torch.randn(1, 2, 3)

k = torch.randn(2, 3, 4)

v = torch.randn(2, 3, 4)
dropout_p = 1

test_inputs = [q, k, v, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 3] but got: [2, 4].

jit:
Failed running call_function <built-in method matmul of type object at 0x78bf3f396ec0>(*(FakeTensor(..., size=(1, s3, s4)), FakeTensor(..., size=(s0, s2, s1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [s0, s4] but got: [s0, s2].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''