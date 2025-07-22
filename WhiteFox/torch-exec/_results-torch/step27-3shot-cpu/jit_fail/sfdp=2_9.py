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
        self.softmax = torch.nn.Softmax(dim=-1)
        self.dropout = torch.nn.Dropout(0.1)

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk / 100000
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = torch.matmul(dropout_qk, value)
        return output


func = Model().to('cpu')


query = torch.randn(20, 256)

key = torch.randn(20, 8, 32)

value = torch.randn(20, 8, 32)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [20, 256] but got: [20, 32].

jit:
Failed running call_function <built-in method matmul of type object at 0x7c9e7b596ec0>(*(FakeTensor(..., size=(s3, s4)), FakeTensor(..., size=(s0, s2, s1))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [s0, s4] but got: [s0, s2].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''