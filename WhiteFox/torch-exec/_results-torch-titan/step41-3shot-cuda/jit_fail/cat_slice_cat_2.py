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
        f1 = []
        size = len(x[0])
        for t in x:
            f1.append(t)
        f2 = torch.cat(f1, dim=1)
        f3 = f2[:, 0:9223372036854775807]
        f4 = f3[:, 0:size]
        f5 = torch.cat([f2, f4], dim=1)
        return f5



func = Model().to('cuda')

x = 1

test_inputs = [x]

# JIT_FAIL
'''
direct:
'int' object is not subscriptable

jit:
'int' object is not subscriptable

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''