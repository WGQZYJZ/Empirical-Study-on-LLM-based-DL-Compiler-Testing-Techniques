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



class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.layers_f = nn.Linear(2, 2)
        self.layers_j = nn.Linear(2, 2)

    def forward(self, x):
        x = self.layers_f(x)
        x = self.layers_j(x)
        x = torch.stack((x, x, x), dim=1)
        x = torch.cat([x, x], dim=1)
        return x




func = Model().to('cuda')



x1 = torch.randn(1, 2)



x2 = torch.randn(1, 2)


test_inputs = [x1, x2]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''