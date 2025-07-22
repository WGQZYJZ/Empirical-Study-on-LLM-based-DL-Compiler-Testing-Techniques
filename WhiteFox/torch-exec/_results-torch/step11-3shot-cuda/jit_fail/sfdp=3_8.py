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
        self.dropout1d = torch.nn.Dropout(0.2)
        self.dropout2d = torch.nn.Dropout2d(0.2)

    def forward(self, q, k, v, scale_factor, dropout_p):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout1d(softmax_qk)
        output = dropout_qk.matmul(v)
        return output



func = Model().to('cuda')


q = torch.randn(1, 21, 1000)

k = torch.randn(1, 21, 1200)

v = torch.randn(1, 21, 1200)
scale_factor = 1
dropout_p = 1

test_inputs = [q, k, v, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [1, 1000] but got: [1, 1200].

jit:
Failed running call_function <built-in method matmul of type object at 0x79fe59196ec0>(*(FakeTensor(..., device='cuda:0', size=(1, 21, 1000)), FakeTensor(..., device='cuda:0', size=(1, s1, s0))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [1, 1000] but got: [1, s1].

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''