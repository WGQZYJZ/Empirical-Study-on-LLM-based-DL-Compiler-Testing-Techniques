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
        self.dropout = torch.nn.Dropout(0.5)
        self.softmax = torch.nn.Softmax(dim=-1)
        self.matmul1 = torch.matmul

    def forward(self, query, key, value, scale_factor, dropout_p):
        qk = self.matmul1(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, value)
        return output


func = Model().to('cpu')


query = torch.randn(1, 4, 16)

key = torch.randn(1, 4, 128)

value = torch.randn(1, 4, 128)
scale_factor = 1
dropout_p = 1

test_inputs = [query, key, value, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 16] but got: [1, 128].

jit:
Failed running call_function <built-in method matmul of type object at 0x7d5898196ec0>(*(FakeTensor(..., size=(1, 4, 16)), FakeTensor(..., size=(1, 128, 4))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 16] but got: [1, 128].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''