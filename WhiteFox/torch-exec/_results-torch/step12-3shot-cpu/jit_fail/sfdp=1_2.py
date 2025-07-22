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
        self.key = torch.nn.Linear(8, 8)
        self.query = torch.nn.Linear(8, 8)
        self.value = torch.nn.Linear(8, 8)

    def forward(self, q1, k1, v1):
        qk = torch.matmul(q1, k1.transpose(-2, -1))
        inv_scale_factor = math.sqrt(64)
        scaled_qk = qk.div(inv_scale_factor)
        dropout_p = 0.1
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(scaled_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model().to('cpu')


q1 = torch.randn(1, 8)

k1 = torch.randn(1, 8)

v1 = torch.randn(1, 8)

test_inputs = [q1, k1, v1]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [8, 1] but got: [8, 64].

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(1, 1)), FakeTensor(..., size=(1, 8, 64, 64))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [8, 1] but got: [8, 64].

from user code:
   File "<string>", line 28, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''