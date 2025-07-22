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

    def forward(self, query, key, value, scale_factor, dropout_p):
        v0 = query.matmul(key.transpose(-2, -1))
        v1 = v0 * scale_factor
        v2 = F.softmax(v1, dim=-1)
        v3 = F.dropout(v2, p=dropout_p)
        v4 = v3.matmul(value)
        return v4


func = Model().to('cpu')


query = torch.randn(1, 64, 128)

key = torch.randn(1, 128, 64)

value = torch.randn(1, 128, 64)
scale_factor = 1
dropout_p = 1

test_inputs = [query, key, value, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 64].

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(1, 64, 128)), FakeTensor(..., size=(1, 64, 128))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 64].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''