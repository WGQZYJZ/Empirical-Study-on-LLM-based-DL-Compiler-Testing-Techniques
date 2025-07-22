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

    def forward(self, query, key, inv_scale_factor, dropout_p=0.0):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(8, 4, 1, 1)

key = torch.randn(8, 4, 1, 1)
inv_scale_factor = 1

test_inputs = [query, key, inv_scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [32, 1] but got: [32, 512].

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(s0, s1, 1, 1)), FakeTensor(..., size=(1, 1, 512, 4))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [s0*s1, 1] but got: [s0*s1, 512].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''