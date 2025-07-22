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
        self.linear = torch.nn.Linear(8, 2)

    def forward(self, x1, t2):
        v1 = self.linear(x1)
        v3 = (v1 + t2)
        v4 = functional.relu(v3)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 8)



t2 = torch.tensor(3)


test_inputs = [x1, t2]

# JIT_FAIL
'''
direct:
name 'functional' is not defined

jit:
name 'functional' is not defined

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''