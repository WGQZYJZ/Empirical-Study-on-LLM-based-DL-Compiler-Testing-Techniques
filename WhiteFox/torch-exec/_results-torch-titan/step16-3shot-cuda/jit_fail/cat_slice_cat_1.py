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

    def forward(self, x1, x2, x3):
        x1_tmp = torch.cat([x1, x2], dim=1)
        x2_cat_tmp = x1_tmp[:, (- 1)]
        x3_cat = torch.cat([x2_cat_tmp, x3], dim=1)
        return x3_cat



func = Model().to('cuda')



x1 = torch.randn(1, 4)



x2 = torch.randn(1, 8)



x3 = torch.randn(1, 1)


test_inputs = [x1, x2, x3]

# JIT_FAIL
'''
direct:
Dimension out of range (expected to be in range of [-1, 0], but got 1)

jit:
Failed running call_function <built-in method cat of type object at 0x7687c2c699e0>(*([FakeTensor(..., device='cuda:0', size=(1,)), FakeTensor(..., device='cuda:0', size=(1, 1))],), **{'dim': 1}):
Dimension out of range (expected to be in range of [-1, 0], but got 1)

from user code:
   File "<string>", line 23, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''