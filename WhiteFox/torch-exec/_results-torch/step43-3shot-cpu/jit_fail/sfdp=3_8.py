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

    def __init__(self, dropout_p=0.5):
        super().__init__()
        self.dropout_p = dropout_p

    def forward(self, query, key, value, scale_factor):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(2, 64, 512)

key = torch.randn(2, 64, 1024)

value = torch.randn(2, 64, 1024)
scale_factor = 1

test_inputs = [query, key, value, scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 512] but got: [2, 1024].

jit:
Failed running call_function <built-in method matmul of type object at 0x7aac46b96ec0>(*(FakeTensor(..., size=(2, 64, 512)), FakeTensor(..., size=(2, 1024, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 512] but got: [2, 1024].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''