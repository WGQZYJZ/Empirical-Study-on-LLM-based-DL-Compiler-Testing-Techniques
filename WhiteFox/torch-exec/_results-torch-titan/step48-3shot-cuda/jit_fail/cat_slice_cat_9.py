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

    def forward(self, *inputs):
        inputs = torch.cat(inputs, dim=1)
        t1 = inputs[:, 0:9223372036854775807]
        t2 = t1[:, 0:3]
        t3 = t2[:, 1]
        t4 = t3.expand(9223372036854775807, 3)
        inputs = torch.cat([inputs, t4], dim=1)
        return inputs



func = Model().to('cuda')

input_tensor = torch.randn(1, 1, 1)

test_inputs = [input_tensor]

# JIT_FAIL
'''
direct:
index 1 is out of bounds for dimension 1 with size 1

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., device='cuda:0', size=(1, 1, 1)), (slice(None, None, None), 1)), **{}):
index 1 is out of bounds for dimension 1 with size 1

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''