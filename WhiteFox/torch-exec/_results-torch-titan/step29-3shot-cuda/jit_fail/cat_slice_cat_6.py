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

    def forward(self, x):
        a1 = x[0]
        a2 = x[1]
        a3 = torch.cat([a1, a2], dim=1)
        a4 = a3[:, 0:9223372036854775807]
        a5 = a4[:, 0:32]
        a6 = torch.cat([a3, a5], dim=1)
        return a6



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
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''