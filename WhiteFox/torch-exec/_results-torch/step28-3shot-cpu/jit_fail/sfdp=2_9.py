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

    def forward(self, q, k, v, mask, inv_scale_factor, dropout_p):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output


func = Model().to('cpu')


q = torch.randn(2, 4, 512)

k = torch.randn(2, 512, 4)

v = torch.randn(2, 512, 512)


__mask__ = torch.empty(2, 4, dtype=int).random_(2)


__inv_scale_factor__ = torch.empty(1, dtype=torch.float).fill_(0)


__dropout_p__ = torch.empty(1, dtype=torch.float).fill_(0)

test_inputs = [q, k, v, __mask__, __inv_scale_factor__, __dropout_p__]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 512] but got: [2, 4].

jit:
Failed running call_function <built-in method matmul of type object at 0x7b9fa4f96ec0>(*(FakeTensor(..., size=(2, 4, 512)), FakeTensor(..., size=(2, 4, 512))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 512] but got: [2, 4].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''