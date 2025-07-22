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
        self.conv1 = torch.nn.Conv2d(3, 3, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        return v1




func = Model().to('cuda')



x1 = torch.randn(1, 3, 224, 224)



dummy_input = torch.randn(1, 3, 224, 224)


test_inputs = [x1, dummy_input]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''