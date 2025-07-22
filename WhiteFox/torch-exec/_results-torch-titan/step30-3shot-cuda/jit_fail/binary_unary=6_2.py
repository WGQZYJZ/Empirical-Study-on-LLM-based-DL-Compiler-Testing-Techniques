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
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 - torch.randn(v1.__shape__.dim(0), v1.__shape__.dim(1)).to(v1.device))
        v3 = v2.__call__('relu')
        return v3



func = Model().to('cuda')



x1 = torch.randn(1, 3)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Tensor' object has no attribute '__shape__'

jit:
'Tensor' object has no attribute '__shape__'
'''