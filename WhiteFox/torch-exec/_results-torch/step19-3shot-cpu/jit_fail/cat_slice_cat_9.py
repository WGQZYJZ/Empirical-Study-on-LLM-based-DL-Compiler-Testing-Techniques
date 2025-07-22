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

    def forward(self, x):
        v1 = torch.cat([x[0], x[1], x[2]], 1)
        v2 = v1[:, :]
        v3 = v1[:, :]
        v4 = torch.cat([v1, v3], 1)
        return v4


func = Model().to('cpu')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
'int' object is not subscriptable

jit:
TypeError: 'int' object is not subscriptable

from user code:
   File "<string>", line 19, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''