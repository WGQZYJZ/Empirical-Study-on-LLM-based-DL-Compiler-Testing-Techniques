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

    def forward(self, x1, x2):
        return torch.cat(1.1)



func = Model().to('cpu')


x1 = torch.randn(1, 2)

x2 = torch.randn(1, 2)

test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
cat(): argument 'tensors' (position 1) must be tuple of Tensors, not float

jit:
cat(): argument 'tensors' (position 1) must be tuple of Tensors, not float
'''