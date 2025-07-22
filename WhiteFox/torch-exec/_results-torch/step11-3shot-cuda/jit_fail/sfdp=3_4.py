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

    def forward(self, q1, k2, v3):
        qk = torch.matmul(q1, k2.transpose(-2, -1))
        scale_factor = torch.rsqrt(torch.tensor(self.head_dim).float())
        v4 = qk.mul(scale_factor)
        softmax_qk = v4.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        v6 = dropout_qk.matmul(v3)
        return v6


func = Model().to('cuda')

q1 = 1
k2 = 1
v3 = 1

test_inputs = [q1, k2, v3]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'transpose'

jit:
AttributeError: 'int' object has no attribute 'transpose'

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''