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
        self.dropout1 = torch.nn.Dropout(p=0.6)
        self.dropout2 = torch.nn.Dropout(p=0.6)
        self.dropout3 = torch.nn.Dropout(p=0.7)
        self.dropout4 = torch.nn.Dropout(p=0.8)

    def forward(self, x1, x2, x3, x4):
        v1 = torch.linalg.matvec(x1, x2)
        v2 = (v1 * 0.5)
        v3 = (x3 * v2)
        v4 = self.dropout1(torch.tanh(v3))
        v5 = (x4 + v4)
        v6 = self.dropout2(torch.tanh(v5))
        v7 = (v6 * v4)
        v8 = self.dropout3(torch.tanh(v7))
        v9 = (v8 * x3)
        v10 = self.dropout4(torch.tanh(v9))
        v11 = (v10 * v7)
        v12 = (v11 * x4)
        v13 = (v12 * x2)
        v14 = (v13 * x4)
        return v14




func = Model().to('cuda')

x1 = 1
x2 = 1
x3 = 1
x4 = 1

test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
module 'torch.linalg' has no attribute 'matvec'

jit:
module 'torch.linalg' has no attribute 'matvec'

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''