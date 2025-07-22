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

    def __init__(self, scale_factor=1.0, dropout_p=0.0):
        super().__init__()
        self.dropout_p = dropout_p
        self.scale_factor = scale_factor

    def forward(self, queries, keys, values):
        qk = queries.matmul(keys.transpose((- 2), (- 1)))
        scaled_qk = (qk * self.scale_factor)
        softmax_qk = torch.nn.functional.softmax(scaled_qk.mul((- 1)), dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(values)
        return output



func = Model(1.0, 0.0).to('cuda')



query = torch.randn(1, 8, 16)



key = torch.randn(1, 8, 100)

queries = 1

test_inputs = [query, key, queries]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 16] but got: [1, 100].

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 8, 16)), FakeTensor(..., device='cuda:0', size=(1, 100, 8))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 16] but got: [1, 100].

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''