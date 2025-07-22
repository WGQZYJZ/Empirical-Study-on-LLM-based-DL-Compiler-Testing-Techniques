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

    def forward(self, q, k, v, padding_mask, dropout_p):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scale_factor = math.sqrt(float(q.shape[-1]))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        output = torch.where(padding_mask, query, output).long()
        return output


func = Model().to('cpu')


query = torch.randn(1, 23, 768)

key = torch.randn(90, 23, 512)
key = torch.randn(90, 23, 512)
query = torch.randn(1, 23, 768)

batch_size = 1

padding_mask = torch.zeros((batch_size, query.shape[1], key.shape[1]), dtype=torch.bool)
q = 1
k = 1

test_inputs = [query, key, padding_mask, q, k]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [90, 768] but got: [90, 512].

jit:
Failed running call_function <built-in method matmul of type object at 0x7c1ba6796ec0>(*(FakeTensor(..., size=(1, 23, 768)), FakeTensor(..., size=(90, 512, 23))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [90, 768] but got: [90, 512].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''