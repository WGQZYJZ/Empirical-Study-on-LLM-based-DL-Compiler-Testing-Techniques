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

    def forward(self, x, __input_tensor__):
        v0 = torch.cat([x, __input_tensor__], dim=1)
        v1 = torch.cat([v0], dim=1)
        return v1


func = Model().to('cpu')


x = torch.randn(20, 16, 28, 28)
__input_tensor__ = 1

test_inputs = [x, __input_tensor__]

# JIT_FAIL
'''
direct:
expected Tensor as element 1 in argument 0, but got int

jit:
expected Tensor as element 1 in argument 0, but got int
'''