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
        self.key = torch.nn.Linear(64, 64)
        self.query = torch.nn.Linear(64, 64)
        self.value = torch.nn.Linear(64, 64)
        self.scale_factor = torch.nn.Parameter(torch.empty(1))
        torch.nn.init.ones_(self.scale_factor)

    def forward(self, x1, x2, x3):
        qk = torch.matmul(self.query(x1), self.key(x2).transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=x3)
        output = dropout_qk.matmul(self.value(x3))
        return output


func = Model().to('cpu')


x1 = torch.randn(1, 64)

x2 = torch.randn(1, 64)

x3 = torch.randn(1, 64)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Boolean value of Tensor with more than one value is ambiguous

jit:
Failed running call_function <function dropout at 0x7c30dc065b80>(*(FakeTensor(..., size=(1, 1)),), **{'p': FakeTensor(..., size=(1, 64))}):
Boolean value of Tensor with more than one value is ambiguous

from user code:
   File "<string>", line 27, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''