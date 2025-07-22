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

    def __init__(self, num_heads, query_dim, key_dim, dropout_p=0.0):
        super().__init__()
        self.num_heads = num_heads
        self.query_proj = torch.nn.Linear(query_dim, (num_heads * key_dim))
        self.key_proj = torch.nn.Linear(key_dim, (num_heads * query_dim))
        self.value_proj = torch.nn.Linear(key_dim, (num_heads * key_dim))
        self.dropout = torch.nn.Dropout(dropout_p)
        self.scaling_factor = math.sqrt((key_dim // num_heads))

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.div(self.scaling_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(value)
        return output




num_heads = 2


query_dim = 2


key_dim = 2

func = Model(num_heads, query_dim, key_dim, dropout_p).to('cuda')



num_heads = 2


query_dim = 2


query = torch.randn(query_dim, num_heads, 4)



num_heads = 2


key_dim = 2


key = torch.randn(key_dim, num_heads, 7)



num_heads = 2


key_dim = 2


value = torch.randn(key_dim, num_heads, 6)


test_inputs = [query, key, value]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 4] but got: [2, 7].

jit:
Failed running call_function <built-in method matmul of type object at 0x74f5afc699e0>(*(FakeTensor(..., device='cuda:0', size=(2, 2, 4)), FakeTensor(..., device='cuda:0', size=(2, 7, 2))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 4] but got: [2, 7].

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''