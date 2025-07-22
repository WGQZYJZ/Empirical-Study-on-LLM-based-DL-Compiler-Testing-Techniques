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

    def forward(self, *args):
        v1 = [arg for arg in args][0]
        v2 = v1[:, :, :, 0:size]
        v4 = [v1, v2]
        v5 = torch.cat(v4, dim=3)
        return v5



func = Model().to('cuda')



x1 = torch.randn(1, 3, 10, 10)



x2 = torch.randn(1, 3, 20, 20)



x3 = torch.randn(1, 3, 30, 30)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
name 'size' is not defined

jit:
name 'size' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''