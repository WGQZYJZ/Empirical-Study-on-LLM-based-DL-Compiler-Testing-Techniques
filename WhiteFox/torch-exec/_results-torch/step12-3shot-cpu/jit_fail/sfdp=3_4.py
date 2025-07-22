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

class Model(nn.Module):

    def __init__(self, dropout_p):
        super().__init__()
        self.dropout_p = dropout_p

    def forward(self, q, k, v, scale_factor):
        qk = F.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor)
        softmax_qk = F.softmax(scaled_qk, dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=self.dropout_p)
        output = F.matmul(dropout_qk, v)
        return output


dropout_p = 0.2
func = Model(dropout_p).to('cpu')


q = torch.randn(1, 8, 64)

k = torch.randn(1, 8, 64)

v = torch.randn(1, 8, 64)
scale_factor = 1

test_inputs = [q, k, v, scale_factor]

# JIT_FAIL
'''
direct:
module 'torch.nn.functional' has no attribute 'matmul'

jit:
AttributeError: module 'torch.nn.functional' has no attribute 'matmul'

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''