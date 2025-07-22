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
        self.dropout = torch.nn.Dropout(p=0.1)

    def forward(self, x1, x2, x3):
        s1 = torch.matmul(x1, x2.transpose(-2, -1)).div(inv_scale_factor)
        s2 = self.dropout(s1.softmax(dim=-1))
        y1 = s2.matmul(x3)
        return y1


func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

x2 = torch.randn(1, 3, 64, 64)

x3 = torch.randn(1, 3, 64, 64)

test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
name 'inv_scale_factor' is not defined

jit:
NameError: name 'inv_scale_factor' is not defined

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''