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

    def __init__(self, dropout_p, inv_scale_factor):
        super().__init__()
        self.dropout_p = dropout_p
        self.inv_scale_factor = inv_scale_factor

    def forward(self, query, key, value):
        qk = query.matmul(key.transpose(-2, -1))
        scaled_qk = qk.div(self.inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output


dropout_p = 1
inv_scale_factor = 1
func = Model(0.1, 0.5).to('cpu')


query = torch.randn(16, 32, 512)

key = torch.randn(16, 32, 256)

value = torch.randn(16, 32, 256)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [16, 512] but got: [16, 256].

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(16, s1, 512)), FakeTensor(..., size=(16, s3, s2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [16, 512] but got: [16, s3].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''