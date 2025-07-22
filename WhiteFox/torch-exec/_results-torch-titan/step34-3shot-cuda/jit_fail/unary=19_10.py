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
        self.relu = torch.nn.ReLU()
        self.linear = torch.nn.Linear(3, 8, bias=True)

    def forward(self, x1):
        v1 = self.linear(x1)
        if __use_sigmoid__:
            v2 = torch.sigmoid(v1)
        else:
            v2 = self.relu(v1)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name '__use_sigmoid__' is not defined

jit:
name '__use_sigmoid__' is not defined

from user code:
   File "<string>", line 24, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''