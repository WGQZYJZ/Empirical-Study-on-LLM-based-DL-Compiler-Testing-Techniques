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
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:input2D.size(2)]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')



input2D = torch.randn(1, 3, 100)



input3D = torch.randn(1, 3, 100, 100)


test_inputs = [input2D, input3D]

# JIT_FAIL
'''
direct:
Tensors must have same number of dimensions: got 3 and 4

jit:
backend='inductor' raised:
AssertionError: 


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''