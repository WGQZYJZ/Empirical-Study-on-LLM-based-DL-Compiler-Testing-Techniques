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

    def forward(self, query, key, value, scale_factor, dropout_p):
        output = torch.matmul(query, key.transpose(-2, -1))
        output = output.div(scale_factor)
        output = torch.nn.functional.softmax(output)
        output = torch.nn.functional.dropout(output, p=dropout_p)
        output = torch.matmul(output, value)
        return output


func = Model().to('cpu')


q = torch.randn(1, 5, 16)

k = torch.randn(1, 5, 24)

v = torch.randn(1, 5, 24)

s = torch.randn(16, 24)
query = 1

test_inputs = [q, k, v, s, query]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 16] but got: [1, 24].

jit:
Failed running call_function <built-in method matmul of type object at 0x76c671196ec0>(*(FakeTensor(..., size=(1, s2, s3)), FakeTensor(..., size=(1, s1, s0))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, s3] but got: [1, s1].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''