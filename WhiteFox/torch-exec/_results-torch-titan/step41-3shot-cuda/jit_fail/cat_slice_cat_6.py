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

    def forward(self, x1, x2, x3, x4):
        v1 = torch.cat(input_tensors, dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size]
        return torch.cat([v1, v3], dim=1)



func = Model().to('cuda')



x1 = torch.randn(1, 1, 28, 28)



x2 = torch.randn(1, 1, 28, 28)



x3 = torch.randn(1, 1, 28, 28)



x4 = torch.randn(1, 1, 28, 28)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
name 'input_tensors' is not defined

jit:
name 'input_tensors' is not defined

from user code:
   File "<string>", line 18, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''