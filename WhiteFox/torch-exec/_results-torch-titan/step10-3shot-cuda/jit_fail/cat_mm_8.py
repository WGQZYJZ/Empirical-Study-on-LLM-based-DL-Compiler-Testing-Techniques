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
        v1 = (((x1[:, 0].norm() - x2[0].norm()) + x1[:, 1].norm()) - x2[1].norm())
        return torch.cat([v1, v1], 1)




func = Model().to('cuda')



x1 = torch.randn(2, 1)



x2 = torch.randn(2, 1)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
index 1 is out of bounds for dimension 1 with size 1

jit:
Failed running call_function <built-in function getitem>(*(FakeTensor(..., device='cuda:0', size=(2, 1)), (slice(None, None, None), 1)), **{}):
index 1 is out of bounds for dimension 1 with size 1

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''