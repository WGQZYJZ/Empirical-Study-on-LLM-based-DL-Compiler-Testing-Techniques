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

    def forward(self, q, k, v, scale_factor=1.0, dropout_p=0.1):
        qk = torch.matmul(q, k.transpose((- 2), (- 1)))
        scaled_qk = (qk * scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = F.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')



qkv_size = 64


num_heads = 8


batch_size = 1


query = torch.randn(batch_size, num_heads, qkv_size)



qkv_size = 64


num_heads = 8


batch_size = 1


key = torch.randn(batch_size, num_heads, qkv_size)

q = 1
k = 1
v = 1

test_inputs = [query, key, q, k, v]

# JIT_FAIL
'''
direct:
matmul(): argument 'other' (position 1) must be Tensor, not int

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 8, 8)), 1), **{}):
matmul(): argument 'other' (position 1) must be Tensor, not int

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''