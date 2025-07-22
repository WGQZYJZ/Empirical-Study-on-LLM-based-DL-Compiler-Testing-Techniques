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

    def forward(self, query, key, value, scale_factor, dropout_p=0.3):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_dot_product_attention = qk * scale_factor
        softmax_qk = softmax(scaled_dot_product_attention, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output


func = Model().to('cuda')


query = torch.randn(1, 20, 256)

key = torch.randn(1, 10, 20)

value = torch.randn(1, 10, 30)

__scale_factor__ = torch.Tensor([0.1])
scale_factor = 1

test_inputs = [query, key, value, __scale_factor__, scale_factor]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 256] but got: [1, 20].

jit:
Failed running call_function <built-in method matmul of type object at 0x7c9476396ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 20, 256)), FakeTensor(..., device='cuda:0', size=(1, 20, 10))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 256] but got: [1, 20].

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''