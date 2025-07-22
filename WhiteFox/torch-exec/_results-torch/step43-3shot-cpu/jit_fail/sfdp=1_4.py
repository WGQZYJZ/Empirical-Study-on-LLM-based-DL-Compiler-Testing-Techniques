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
        self.dropout_p = 0.0

    def forward(self, x2):
        v2 = x2[0]
        v3 = x2[1]
        v4 = (v2[0] - v2[2]).abs()
        v5 = v4 * v3
        v6 = v2[1]
        v7 = v2[1] - v2[2]
        v8 = torch.nn.functional.relu(v5)
        v9 = v8 + v6
        v11 = torch.nn.functional.relu(v7)
        v12 = v9 / v11
        return v12


func = Model().to('cpu')

x2 = 1

test_inputs = [x2]

# JIT_FAIL
'''
direct:
'int' object is not subscriptable

jit:
TypeError: 'int' object is not subscriptable

from user code:
   File "<string>", line 20, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''