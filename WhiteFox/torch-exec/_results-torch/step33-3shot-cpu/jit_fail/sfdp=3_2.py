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
        self.scale_factor = torch.nn.Parameter(torch.tensor([3.0]))

    def forward(self, q1, k1, v1):
        v = q1.matmul(k1.transpose(-2, -1))
        scale_v = self.scale_factor * v
        softmax = scale_v.softmax(dim=-1)
        dropout = torch.nn.functional.dropout(softmax, p=0.5)
        out = dropout.matmul(v1)
        return out


func = Model().to('cpu')

q1 = 1
k1 = 1
v1 = 1

test_inputs = [q1, k1, v1]

# JIT_FAIL
'''
direct:
'int' object has no attribute 'matmul'

jit:
AttributeError: 'int' object has no attribute 'matmul'

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''