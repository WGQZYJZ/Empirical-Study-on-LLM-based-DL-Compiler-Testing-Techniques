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
        self.linear1 = torch.nn.Linear(14, 8)
        self.linear2 = torch.nn.Linear(8, 10)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = self.linear2(v1)
        v3 = (v2 + other_tensor)
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 14)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'other_tensor' is not defined

jit:
name 'other_tensor' is not defined

from user code:
   File "<string>", line 25, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''