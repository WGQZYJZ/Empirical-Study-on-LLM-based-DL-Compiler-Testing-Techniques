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

    def forward(self, *input_tensors):
        t1 = torch.cat(input_tensors, dim=1)
        t2 = t1[:, (- 1)]
        t3 = t2[:, 112]
        t4 = torch.cat([t1, t3], dim=1)
        return t4



func = Model().to('cuda')



x1 = torch.randn(1, 2)



x2 = torch.randn(1, 3)



x3 = torch.randn(1, 4)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
too many indices for tensor of dimension 1

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., device='cuda:0', size=(1,)), (slice(None, None, None), 112)), **{}):
too many indices for tensor of dimension 1

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''