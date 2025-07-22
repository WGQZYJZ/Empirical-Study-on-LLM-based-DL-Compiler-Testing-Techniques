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
        self.layers = torch.nn.Sequential(torch.nn.Linear(((64 * 64) * 3), 128), torch.nn.ReLU(), torch.nn.Linear(128, 128), torch.nn.ReLU(), torch.nn.Linear(128, 10))

    def forward(self, x1, x2):
        v1 = self.layers[0](x2)
        v2 = (v1 + x1)
        for layer in self.layers[1:]:
            v1 = layer(v2)
            v2 = (v1 + v2)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, ((64 * 64) * 3))



x2 = torch.randn(1, 128)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x128 and 12288x128)

jit:
Failed running call_module sub0_0(*(FakeTensor(..., device='cuda:0', size=(1, 128)),), **{}):
a and b must have same reduction dim, but got [1, 128] X [12288, 128].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''