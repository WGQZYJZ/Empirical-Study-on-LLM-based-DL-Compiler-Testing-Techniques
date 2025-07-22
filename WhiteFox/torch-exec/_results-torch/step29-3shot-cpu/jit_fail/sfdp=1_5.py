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

    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.qkv = torch.nn.Linear(input_dim, output_dim * 2)

    def forward(self, x1):
        qkv = self.qkv(x1)
        (q, k, v) = torch.chunk(qkv, 3, 2)
        q_k = torch.matmul(q, k.transpose(-2, -1))
        scaled_q_k = q_k / np.sqrt(512.0)
        softmax_q_k = scaled_q_k.softmax(dim=-1)
        dropout_q_k = torch.nn.functional.dropout(softmax_q_k, p=dropout_p)
        output = torch.matmul(dropout_q_k, v)
        return output


input_dim = 1
output_dim = 1
func = Model(512, 128).to('cpu')


x1 = torch.randn(8, 512)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-2, 1], but got 2)

jit:
Failed running call_function <built-in method chunk of type object at 0x7f0957b96ec0>(*(FakeTensor(..., size=(8, 256)), 3, 2), **{}):
Dimension out of range (expected to be in range of [-2, 1], but got 2)

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''