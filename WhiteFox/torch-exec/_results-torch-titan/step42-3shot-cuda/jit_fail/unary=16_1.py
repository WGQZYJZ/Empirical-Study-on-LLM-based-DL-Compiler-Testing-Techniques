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
        self.l1 = torch.nn.Linear(3, 2)

    def forward(self, x1):
        x2 = self.l1(torch.cat([x1, x1], dim=1))
        x3 = torch.nn.functional.gptj_gelu(x2)
        x4 = torch.nn.functional.gptj_gelu(x2)
        x5 = torch.nn.functional.gptj_gelu(x2)
        x6 = torch.nn.functional.gptj_gelu(x2)
        x7 = torch.nn.functional.gptj_gelu(x2)
        x8 = torch.nn.functional.gptj_gelu(x2)
        x9 = torch.nn.functional.gptj_gelu(x2)
        x10 = torch.nn.functional.gptj_gelu(x2)
        x11 = torch.nn.functional.gptj_gelu(x2)
        return (x3, x4, x5, x6, x7, x8, x9, x10, x11)



func = Model().to('cuda')



x1 = torch.randn(1, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
mat1 and mat2 shapes cannot be multiplied (1x6 and 3x2)

jit:
Failed running call_module L__self___l1(*(FakeTensor(..., device='cuda:0', size=(1, 6)),), **{}):
a and b must have same reduction dim, but got [1, 6] X [3, 2].

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''