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

    def forward(self, q, k, v):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output


func = Model().to('cpu')


q = torch.randn(10, 12, 64)

k = torch.randn(10, 12, 64)

v = torch.randn(10, 12, 64)

test_inputs = [q, k, v]

# JIT_FAIL
'''
direct:
The size of tensor a (10) must match the size of tensor b (8) at non-singleton dimension 1

jit:
Failed running call_method mul(*(FakeTensor(..., size=(10, 12, 12)), FakeTensor(..., size=(1, 8, 1, 1))), **{}):
Attempting to broadcast a dimension of length 8 at -3! Mismatching argument at index 1 had torch.Size([1, 8, 1, 1]); but expected shape should be broadcastable to [1, 10, 12, 12]

from user code:
   File "<string>", line 17, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''