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

    def forward(self, x):
        y = torch.cat((x, x, x, x), dim)
        y = torch.relu(y)
        y = torch.reshape(y, ((- 1), 8))
        y = y.mean(dim=0)
        return y




func = Model().to('cuda')



x = torch.randn(1, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
name 'dim' is not defined

jit:
name 'dim' is not defined

from user code:
   File "<string>", line 21, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''