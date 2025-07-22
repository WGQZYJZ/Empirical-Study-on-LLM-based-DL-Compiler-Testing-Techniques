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

    def forward(self, query, key, value, dim=-1, scale_factor=1.0, dropout_p=0.0):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=dim)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return dropout_qk.matmul(value)


func = Model().to('cpu')


query = torch.rand(1, 3, 4, 32)

key = torch.rand(1, 3, 32, 16)

value = torch.rand(1, 3, 4, 16)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [3, 32] but got: [3, 16].

jit:
Failed running call_function <built-in method matmul of type object at 0x7f0cc8f96ec0>(*(FakeTensor(..., size=(1, 3, 4, 32)), FakeTensor(..., size=(1, 3, 16, 32))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [3, 32] but got: [3, 16].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''