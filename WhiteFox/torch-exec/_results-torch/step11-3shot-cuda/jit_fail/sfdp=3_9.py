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

    def __init__(self, dropout_p=0.9):
        super().__init__()
        self.dropout_p = dropout_p

    def forward(self, query, key, value):
        scale_factor = np.sqrt(query.size(-1))
        qk = query.matmul(key.transpose(-1, -2))
        v1 = qk.mul(scale_factor)
        v2 = v1.softmax(dim=-1)
        v3 = torch.nn.functional.dropout(v2, p=self.dropout_p)
        return v3.matmul(value)


func = Model().to('cuda')


query = torch.randn(1, 5, 15, 15)

key = torch.randn(1, 5, 15, 15)

value = torch.randn(1, 5, 10, 10)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [5, 15] but got: [5, 10].

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 5, 15, 15)), FakeTensor(..., device='cuda:0', size=(1, 5, 10, 10))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [5, 15] but got: [5, 10].

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''