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
        self.query = torch.nn.Parameter(torch.randn(8, 8, 10))
        self.key = torch.nn.Parameter(torch.randn(8, 8, 15))
        self.value = torch.nn.Parameter(torch.randn(8, 8, 20))

    def forward(self, x, dropout_p=0.1):
        q = self.query
        k = self.key
        v = self.value
        scale_factor = torch.tensor(15)
        inv_scale_factor = torch.div(scale_factor, torch.tensor(1e-08))
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output


func = Model().to('cpu')


x1 = torch.randn(8, 8, 10)
x = 1

test_inputs = [x1, x]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [8, 10] but got: [8, 15].

jit:
Failed running call_function <built-in method matmul of type object at 0x7d2ce0d96ec0>(*(Parameter(FakeTensor(..., size=(8, 8, 10), requires_grad=True)), FakeTensor(..., size=(8, 15, 8), requires_grad=True)), **{}):
Expected size for first two dimensions of batch2 tensor to be: [8, 10] but got: [8, 15].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''