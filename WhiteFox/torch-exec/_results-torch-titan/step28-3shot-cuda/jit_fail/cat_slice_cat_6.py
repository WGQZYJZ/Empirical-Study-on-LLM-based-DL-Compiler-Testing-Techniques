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

    def forward(self, x1):
        v1 = torch.cat([x1[0], x1[1]], dim=1)
        v2 = v1[:, 0:9223372036854775802]
        v3 = v2[:, 0:16]
        v4 = torch.cat([v1, v3], dim=1)
        v5 = torch.nn.functional.relu(v4)
        v6 = torch.reshape(v5, [1, 1, 4, 4])
        v7 = torch.cat([v6, v1], dim=1)
        v8 = torch.reshape(v7, [1, 13, 1, 1])
        v9 = torch.cat([v8, x1[2]], dim=1)
        return v9



func = Model().to('cuda')

x1 = 1

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'int' object is not subscriptable

jit:
'int' object is not subscriptable

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''