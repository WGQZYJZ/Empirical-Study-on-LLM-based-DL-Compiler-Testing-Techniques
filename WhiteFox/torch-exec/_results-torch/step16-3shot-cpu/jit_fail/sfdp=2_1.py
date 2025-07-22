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

    def __init__(self, dropout_p=0.5, n_heads=8):
        super().__init__()
        self.dropout_p = dropout_p
        self.n_heads = n_heads

    def forward(self, query, key, value, mask=None):
        scaled_qk = torch.matmul(query, key.transpose(-2, -1))
        inv_scale_factor = torch.sqrt(torch.tensor(key.shape[-1], dtype=torch.float16))
        softmax_qk = scaled_qk / inv_scale_factor
        softmax_qk = softmax_qk.softmax(dim=-1)
        dropout = torch.nn.functional.dropout(softmax_qk, self.dropout_p)
        output = dropout.matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(1, 32, 128)

key = torch.randn(1, 32, 256)

value = torch.randn(1, 32, 256)

test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 256].

jit:
Failed running call_function <built-in method matmul of type object at 0x7e631af96ec0>(*(FakeTensor(..., size=(1, 32, 128)), FakeTensor(..., size=(1, 256, 32))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 128] but got: [1, 256].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''