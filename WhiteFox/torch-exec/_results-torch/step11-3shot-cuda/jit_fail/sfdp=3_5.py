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
        self.dropout = torch.nn.Dropout(p=0.0)

    def forward(self, q, k, v, scale_factor, dropout_p):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = self.dropout(softmax_qk).mul(dropout_p)
        output = dropout_qk.matmul(v)
        return output


func = Model().to('cuda')


q = torch.randn(2, 6, 5)

k = torch.randn(2, 4, 6)

v = torch.randn(2, 4, 5)

scale_factor = torch.randn(12, 5)
dropout_p = 1

test_inputs = [q, k, v, scale_factor, dropout_p]

# JIT_FAIL
'''
direct:
Expected size for first two dimensions of batch2 tensor to be: [2, 5] but got: [2, 6].

jit:
Failed running call_function <built-in method matmul of type object at 0x79fe59196ec0>(*(FakeTensor(..., device='cuda:0', size=(2, 6, 5)), FakeTensor(..., device='cuda:0', size=(2, 6, 4))), **{}):
Expected size for first two dimensions of batch2 tensor to be: [2, 5] but got: [2, 6].

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''