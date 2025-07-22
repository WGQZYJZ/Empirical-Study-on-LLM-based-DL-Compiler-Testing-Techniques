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
        y = torch.cat((x, torch.zeros(2, 3, 4)), dim=1)
        y = y.view(y.shape[0], -1) if y.shape[1] != 4 else y.view(y.shape[0], -2)
        y = y.view(y.shape[0], -1)
        return torch.where(x < 0.0, tensor1, tensor2)



func = Model().to('cpu')


x = torch.randn(2, 3, 4)

test_inputs = [x]

# JIT_FAIL
'''
direct:
name 'tensor1' is not defined

jit:
NameError: name 'tensor1' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''