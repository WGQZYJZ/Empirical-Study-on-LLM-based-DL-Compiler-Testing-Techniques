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

    def forward(self, query, key, value, key_padding_mask, attn_mask, memory_mask, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(0.32)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cpu')


query = torch.randn(2, 5, 3, 512)

key = torch.randn(2, 5, 128, 36)

value = torch.randn(2, 5, 128, 36)


key_padding_mask = torch.randn(2, 5, 128, 36).to(dtype=torch.bool)


attn_mask = torch.randn(2, 5, 512, 512).to(dtype=torch.bool)


memory_mask = torch.randn(2, 5, 23, 36).to(dtype=torch.bool)
dropout_p = 1

test_inputs = [query, key, value, key_padding_mask, attn_mask, memory_mask, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [10, 512] but got: [10, 36].

jit:
Failed running call_function <built-in method matmul of type object at 0x7bf95f996ec0>(*(FakeTensor(..., size=(2, 5, 3, 512)), FakeTensor(..., size=(2, 5, 36, 128))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [10, 512] but got: [10, 36].

from user code:
   File "<string>", line 16, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''