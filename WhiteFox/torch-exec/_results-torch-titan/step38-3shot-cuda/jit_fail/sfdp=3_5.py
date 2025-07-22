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
        self.dropout_p = 0.5

    def forward(self, x):
        query = x
        key = x
        scale_factor = (query.size(1) ** (- 0.5))
        qk = torch.matmul(query, key.transpose((- 2), (- 1)))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=(- 1))
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output



func = Model().to('cuda')



x = torch.randn(1, 16, 10, 10)


test_inputs = [x]

# JIT_FAIL
'''
direct:
The size of tensor a (16) must match the size of tensor b (3) at non-singleton dimension 1

jit:
Failed running call_method matmul(*(FakeTensor(..., device='cuda:0', size=(1, 16, 10, 10)), FakeTensor(..., size=(1, 3, 10, 10))), **{}):
Shape mismatch: objects cannot be broadcast to a single shape

from user code:
   File "<string>", line 29, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''