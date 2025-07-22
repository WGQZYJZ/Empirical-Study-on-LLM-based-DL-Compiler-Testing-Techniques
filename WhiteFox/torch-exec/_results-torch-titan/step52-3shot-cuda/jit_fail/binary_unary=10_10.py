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

    def __init__(self, in_shape, out_channels):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(in_shape, out_channels)

    def forward(self, x):
        return relu((self.linear(x) + x))



in_shape = 1
out_channels = 1
func = Model(4, 8).to('cuda')



x1 = torch.randn(1, 4)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
name 'relu' is not defined

jit:
name 'relu' is not defined

from user code:
   File "<string>", line 22, in forward


You can suppress this exception and fall back to eager by setting:
    import torch._dynamo
    torch._dynamo.config.suppress_errors = True

'''