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
        self.dropout = torch.nn.Dropout(1)

    def forward(self, query, key, value, scale_factor=1):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(1, 2, 3)

key = torch.randn(1, 3, 4)

value = torch.randn(1, 3, 4)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 3] but got: [1, 4].

jit:
Failed running call_function <built-in method matmul of type object at 0x72c734396ec0>(*(FakeTensor(..., size=(1, 2, 3)), FakeTensor(..., size=(1, 4, 3))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 3] but got: [1, 4].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''