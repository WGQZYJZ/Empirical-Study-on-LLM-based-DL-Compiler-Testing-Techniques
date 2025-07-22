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

    def __init__(self, scale_factor=None, dropout_p=0):
        super().__init__()
        self.scale_factor = scale_factor
        self.dropout_p = dropout_p

    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        if self.scale_factor != None:
            qk = qk.mul(self.scale_factor)
        softmax_qk = qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
        return output


func = Model(scale_factor=1, dropout_p=0.1).to('cpu')


x1 = torch.randn(10, 32, 64)

x2 = torch.randn(10, 32, 64)

x3 = torch.randn(10, 64, 32)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [10, 32] but got: [10, 64].

jit:
Failed running call_method matmul(*(FakeTensor(..., size=(10, 32, 32)), FakeTensor(..., size=(10, 64, 32))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [10, 32] but got: [10, 64].

from user code:
   File "<string>", line 26, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''