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

    def forward(self, x1, x2, w1, w2):
        x3 = torch.matmul(x1, x2.transpose(-2, -1))
        x4 = x3 * w1
        x5 = x4.softmax(dim=-1)
        x6 = torch.nn.functional.dropout(x5, p=w2)
        x7 = torch.matmul(x6, w)
        return x7


func = Model().to('cpu')


x1 = torch.randn(3, 5)

x2 = torch.randn(2, 5)

w1 = torch.tensor(2.0)
w2 = 1

test_inputs = [x1, x2, w1, w2]

# JIT_FAIL
'''
direct:
name 'w' is not defined

jit:
NameError: name 'w' is not defined

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''