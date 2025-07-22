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

    def __init__(self, dim=1):
        super().__init__()

    def forward(self, *xs):
        t1 = torch.cat(xs, dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3 = t2[:, 0:xs[0].size(dim)]
        t4 = torch.cat([t1, t3], dim=1)
        return t4



func = Model(dim=1).to('cuda')

input_tensor = torch.randn(1, 1, 1)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
name 'dim' is not defined

jit:
name 'dim' is not defined

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''