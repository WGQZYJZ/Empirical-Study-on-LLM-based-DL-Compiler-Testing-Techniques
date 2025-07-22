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

    def forward(self, x1, x2, x3):
        q = x1.mean(dim=1)
        k = x2.view(x2.shape[0], -1)
        v = x3
        qk = torch.matmul(q, k.transpose(-2, -1))
        inv_scale_factor = math.sqrt(q.shape[-1])
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        p = 0.01
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=p)
        output = dropout_qk.transpose(1, 2).matmul(v).squeeze(-1)
        return output


func = Model().to('cpu')


x1 = torch.randn(12, 16, 8)

x2 = torch.randn(12, 32, 12)

x3 = torch.randn(12, 12, 16)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (12x8 and 384x12)

jit:
Failed running call_function <built-in method matmul of type object at 0x72f828b96ec0>(*(FakeTensor(..., size=(12, 8)), FakeTensor(..., size=(384, 12))), **{}):
a and b must have same reduction dim, but got [12, 8] X [384, 12].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''