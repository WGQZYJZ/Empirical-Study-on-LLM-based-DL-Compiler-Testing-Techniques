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

    def forward(self, qk, dropout):
        softmax_qk = torch.softmax(qk * 0.5, dim=-1)
        output = torch.nn.functional.dropout(softmax_qk, p=dropout).matmul(value)
        return output


func = Model().to('cpu')


query = torch.randn(1, 32, 128)

key = torch.randn(1, 32, 256)

test_inputs = [query, key]

# JIT_FAIL
'''
direct:
Boolean value of Tensor with more than one value is ambiguous

jit:
Failed running call_function <function dropout at 0x72afaa5e3b80>(*(FakeTensor(..., size=(1, 32, 128)),), **{'p': FakeTensor(..., size=(1, 32, 256))}):
Boolean value of Tensor with more than one value is ambiguous

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''