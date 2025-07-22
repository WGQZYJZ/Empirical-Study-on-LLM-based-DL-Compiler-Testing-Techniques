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



class Reshape(torch.nn.Module):

    def __init__(self, t):
        super().__init__()
        self.t = t

    def forward(self, x):
        x = x.view(x.size(0), (- 1))
        y = self.t(x)
        z = y.tanh()
        z = torch.cat([z, z, z], dim=1)
        q = z.view(z.shape[0], (- 1))
        q = q.tanh()



t = 1

func = Reshape(t).to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]

# JIT_FAIL
'''
direct:
'int' object is not callable

jit:
'int' object is not callable
'''