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
        x2 = torch.cat([x1, x1, x1], dim=1)
        x3 = x2[:, 0:9223372036854775807]
        x4 = x3[:, 0:size]
        x5 = torch.cat([x2, x4], dim=1)
        return x5



func = Model().to('cuda')



x1 = torch.randn(1, 400, 7)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'size' is not defined

jit:
name 'size' is not defined

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''