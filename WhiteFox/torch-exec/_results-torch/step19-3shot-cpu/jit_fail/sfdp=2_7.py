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

    def __init__(self, scale_factor, dropout_p):
        super().__init__()
        self.q = torch.randn(8, 64, 32)
        self.k = torch.randn(8, 32, 64)
        self.v = torch.randn(8, 32, 64)
        self.scale_factor = scale_factor
        self.dropout_p = dropout_p

    def forward(self, query):
        qk = torch.matmul(query, self.k.transpose(-2, -1))
        inv_scale_factor = self.scale_factor ** (-1)
        dropout_qk = torch.nn.functional.dropout(qk.softmax(dim=-1) * inv_scale_factor, p=self.dropout_p)
        output = dropout_qk.matmul(self.v)
        return output


scale_factor = 1
dropout_p = 1
func = Model(0.75, 0.3).to('cpu')


query = torch.randn(1, 8, 64, 32)

test_inputs = [query]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [8, 32] but got: [8, 64].

jit:
Failed running call_function <built-in method matmul of type object at 0x705f2c396ec0>(*(FakeTensor(..., size=(1, 8, 64, 32)), FakeTensor(..., size=(8, 64, 32))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [8, 32] but got: [8, 64].

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''