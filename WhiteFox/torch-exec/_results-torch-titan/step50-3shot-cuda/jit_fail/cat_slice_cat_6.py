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
        self.model = torch.nn.Sequential(torch.nn.Conv2d(3, 8, 1), torch.nn.ReLU(), torch.nn.Conv2d(8, 16, 1))

    def forward(self, x1):
        v1 = self.model(x1)
        v2 = torch.cat(list(torch.unbind(v1, dim=1)), dim=1)
        v3 = v2[:, 0:9223372036854775807]
        v4 = v3[:, 0:x1.size(2)]
        v5 = torch.cat((v1, v4), dim=1)
        return v5



func = Model().to('cuda')



x1 = torch.randn(8, 3, 64, 64)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 4 and 3

jit:
backend='inductor' raised:
AssertionError: 


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''