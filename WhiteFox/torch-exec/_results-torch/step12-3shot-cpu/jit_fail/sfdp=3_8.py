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

    def forward(self, x, y, attn_mask, dropout):
        qk = torch.matmul(x, y.transpose(-2, -1))
        scale_factor = attn_mask.to(torch.float) / y.size(-2) ** 0.5
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout)
        output = dropout_qk.matmul(y)
        return output.add(x)


func = Model().to('cpu')


x = torch.randn(1, 5, 1)

y = torch.randn(1, 2, 1)

scale_factor = torch.randn(1, 5, 2).clamp(min=1, max=1.5)

attn_mask = torch.randn(1, 5, 2)

test_inputs = [x, y, scale_factor, attn_mask]

# JIT_FAIL
'''
direct:
Boolean value of Tensor with more than one value is ambiguous

jit:
Failed running call_function <function dropout at 0x7665a9065b80>(*(FakeTensor(..., size=(1, 5, 2)),), **{'p': FakeTensor(..., size=(1, 5, 2))}):
Boolean value of Tensor with more than one value is ambiguous

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''