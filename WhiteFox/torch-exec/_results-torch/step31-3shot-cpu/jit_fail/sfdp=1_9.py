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
        self.output_size = 256

    def forward(self, query, key, value, query_scale_factor=1.0, key_scale_factor=1.0, value_scale_factor=1.0):
        qk = torch.matmul(query, key.transpose(-2, -1)) * query_scale_factor * key_scale_factor
        scaled_qk = torch.div(qk, value_scale_factor)
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.4)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(8, 256, 30)

key = torch.randn(8, 30, 256)

value = torch.randn(8, 256, 256)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [8, 30] but got: [8, 256].

jit:
Failed running call_function <built-in method matmul of type object at 0x78b95b396ec0>(*(FakeTensor(..., size=(8, 256, 30)), FakeTensor(..., size=(8, 256, 30))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [8, 30] but got: [8, 256].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''