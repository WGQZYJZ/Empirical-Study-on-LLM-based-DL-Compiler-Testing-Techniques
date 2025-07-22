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
        self.mul = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:(x2.size(3) * x2.size(3))]
        v4 = torch.cat([v1, v3], dim=1)
        return self.mul(v4)



func = Model().to('cuda')



x1 = torch.randn(1, 2, 4)



x2 = torch.randn(1, 2, 4)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-3, 2], but got 3)

jit:
tuple index out of range

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''