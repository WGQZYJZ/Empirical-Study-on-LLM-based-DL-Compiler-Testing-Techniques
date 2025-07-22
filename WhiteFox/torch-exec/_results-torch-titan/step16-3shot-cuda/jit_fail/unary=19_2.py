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
        self.fc = torch.nn.Linear(8, 2)

    def forward(self, x1):
        v1 = torch.linear(x1)
        va = torch.sigmoid(v1)
        return (va, v1)



func = Model().to('cuda')



x1 = torch.randn(2, 8)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
module 'torch' has no attribute 'linear'

jit:
module 'torch' has no attribute 'linear'

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''