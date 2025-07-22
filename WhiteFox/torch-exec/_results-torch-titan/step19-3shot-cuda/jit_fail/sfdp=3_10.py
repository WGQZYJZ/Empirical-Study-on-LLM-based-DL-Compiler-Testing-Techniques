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

    def __init__(self, num_heads, embedding_size, dropout_p):
        super().__init__()
        self.query_projection = torch.nn.Linear(embedding_size, embedding_size)
        self.key_projection = torch.nn.Linear(embedding_size, embedding_size)
        self.value_projection = torch.nn.Linear(embedding_size, embedding_size)
        self.num_heads = num_heads
        self.dropout_p = dropout_p

    def forward(self, query, key, value, scale_factor):
        q = self.query_projection(query)
        k = self.key_projection(key)
        v = self.value_projection(value)
        q = q.reshape((q.shape[:(- 1)] + (self.num_heads, (q.shape[(- 1)] // self.num_heads)))).transpose(2, 3)
        k = k.reshape((k.shape[:(- 1)] + (self.num_heads, (k.shape[(- 1)] // self.num_heads)))).transpose(2, 3)
        v = v.reshape((v.shape[:(- 1)] + (self.num_heads, (v.shape[(- 1)] // self.num_heads)))).transpose(2, 3)
        q_scaled = q.mul(scale_factor)
        softmax_qk = q_scaled.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(v)
        output = output.transpose(2, 3).reshape((output.shape[:(- 2)] + ((output.shape[2] * output.shape[3]),)))
        return output




num_heads = 2


embedding_size = 24


dropout_p = 0.0

func = Model(num_heads, embedding_size, dropout_p).to('cuda')



embedding_size = 24


embedding_size = 24


query = torch.rand(10, embedding_size, embedding_size)



embedding_size = 24


embedding_size = 24


key = torch.rand(10, embedding_size, embedding_size)



embedding_size = 24


embedding_size = 24


value = torch.rand(10, embedding_size, embedding_size)

scale_factor = 1

test_inputs = [query, key, value, scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [240, 2] but got: [240, 12].

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(10, 24, 12, 2)), FakeTensor(..., device='cuda:0', size=(10, 24, 12, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [240, 2] but got: [240, 12].

from user code:
   File "<string>", line 35, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''