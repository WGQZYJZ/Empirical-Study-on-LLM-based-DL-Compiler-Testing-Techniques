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

    def forward(self, X):
        return torch.mm(X, 2)



func = Model().to('cpu')


X = torch.randn(100, 100)

test_inputs = [X]

# JIT_FAIL
'''
direct:
mm(): argument 'mat2' (position 2) must be Tensor, not int

jit:
mm(): argument 'mat2' (position 2) must be Tensor, not int
'''