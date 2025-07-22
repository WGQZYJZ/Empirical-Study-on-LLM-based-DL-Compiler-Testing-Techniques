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

    def forward(self, x1, x2):
        x3 = torch.cat([x1, x2], dim=1)
        x4 = x3[:, 0:9223372036854775807]
        x5 = x4[:, 0:(((x1.size()[1] * x1.size()[2]) * x1.size()[3]) - size)]
        x6 = torch.cat([x3, x5], dim=1)
        return x6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 64, 64, 64)


test_inputs = [x1, x2]

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