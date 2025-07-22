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
        self.softmax = torch.nn.Softmax(dim=1)

    def forward(self, x1):
        v1 = torch.nn.Flatten()
        v2 = self.softmax(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(2, 16, 2, 2)


test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Flatten' object has no attribute 'softmax'

jit:
'Flatten' object has no attribute 'softmax'
'''