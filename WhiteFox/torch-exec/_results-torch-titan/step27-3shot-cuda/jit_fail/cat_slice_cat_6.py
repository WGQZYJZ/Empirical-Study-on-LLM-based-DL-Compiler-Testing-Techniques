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
        self.constant1 = torch.empty(1)
        self.constant2 = torch.empty(1)
        self.constant3 = torch.empty(1)

    def forward(self, x1):
        t1 = torch.cat([x1, self.constant1, self.constant2], dim=1)
        t2 = t1[:, 1:3]
        t3 = torch.cat([t1, self.constant3], dim=1)
        return torch.cat([t1, t2, t3], dim=1)



func = Model().to('cuda')



x1 = torch.randn(1, 2, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 4 and 1

jit:
backend='inductor' raised:
AssertionError: 


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''