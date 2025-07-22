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
        x = (x.view(int((x.shape[0] / 2)), (- 1)), x.view(int((x.shape[0] / 2)), (- 1)))
        x = x.permute(1, 0, 2).contiguous()
        y = x.view(x.shape[0], (- 1))
        return x




func = Model().to('cuda')



x = torch.randn(10, 16, 28, 28)


test_inputs = [x]

# JIT_FAIL
'''
direct:
'tuple' object has no attribute 'permute'

jit:
'tuple' object has no attribute 'permute'
'''