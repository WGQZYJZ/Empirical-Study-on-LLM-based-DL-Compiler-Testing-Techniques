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

    def __init__(self, dropout):
        super().__init__()
        self.dropout = dropout

    def forward(self, q, k, v, scale_factor):
        k = k.transpose(-2, -1)
        qk = torch.matmul(q, k)
        inv_scale_factor = 1.0 / scale_factor
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout)
        output = dropout_qk.matmul(v)
        return output


dropout = 1
func = Model(dropout_p).to('cpu')


q = torch.randn(2, 8, 64)

k = torch.randn(2, 4, 128)

v = torch.randn(2, 4, 128)

scale_factor = torch.randn(1)

test_inputs = [q, k, v, scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 64] but got: [2, 128].

jit:
Failed running call_function <built-in method matmul of type object at 0x786eac596ec0>(*(FakeTensor(..., size=(2, 8, 64)), FakeTensor(..., size=(2, 128, 4))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 64] but got: [2, 128].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''