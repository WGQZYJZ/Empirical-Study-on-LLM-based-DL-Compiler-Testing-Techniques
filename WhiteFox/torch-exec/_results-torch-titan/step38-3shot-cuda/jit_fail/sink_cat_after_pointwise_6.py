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
        self.conv1d = torch.nn.Conv1d(4, 2, 3)
        self.conv2d = torch.nn.Conv2d(1, 2, 3)
        self.conv3d = torch.nn.Conv3d(1, 2, 3)

    def forward(self, x):
        if (torch.randn(1) > 0.5):
            conv = self.conv1d
        elif (torch.randn(1) > 0.5):
            conv = self.conv2d
        else:
            conv = self.conv3d
        x = conv(x)
        x = x.view(x.shape[0], (- 1)).tanh()
        return x




func = Model().to('cuda')



x = torch.randn(2, 1, 4, 4, 4)



y = torch.randn(4, 2, 3)


test_inputs = [x, y]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''