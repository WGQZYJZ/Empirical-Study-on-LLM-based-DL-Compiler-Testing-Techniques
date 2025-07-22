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
        pass

    def forward(self, q, k, v, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk * inv_scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


q = torch.randn(1, 32, 43)

k = torch.randn(1, 32, 87)

v = torch.randn(1, 32, 98)

inv_scale_factor = torch.tensor(0.001)

x1 = torch.randn(1, 32, 34)

test_inputs = [q, k, v, inv_scale_factor, x1]

# JIT_FAIL
'''
direct:
Boolean value of Tensor with more than one value is ambiguous

jit:
Failed running call_function <function dropout at 0x7f0905ea6b80>(*(FakeTensor(..., size=(1, 512, 64, 64)),), **{'p': FakeTensor(..., size=(1, 32, 34))}):
Boolean value of Tensor with more than one value is ambiguous

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''