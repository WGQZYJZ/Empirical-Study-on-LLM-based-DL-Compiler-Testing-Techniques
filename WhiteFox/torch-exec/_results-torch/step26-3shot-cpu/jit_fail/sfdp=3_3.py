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

    def forward(self, query, key, value, scale_factor=1.0, dropout_p=0.1):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return dropout_qk.matmul(value)


func = Model().to('cpu')


query = torch.randn(1, 1, 50, 150)

key = torch.randn(1, 1, 50, 250)

value = torch.randn(1, 1, 50, 250)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 150] but got: [1, 250].

jit:
Failed running call_function <built-in method matmul of type object at 0x754270f96ec0>(*(FakeTensor(..., size=(1, 1, 50, 150)), FakeTensor(..., size=(1, 1, 250, 50))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 150] but got: [1, 250].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''