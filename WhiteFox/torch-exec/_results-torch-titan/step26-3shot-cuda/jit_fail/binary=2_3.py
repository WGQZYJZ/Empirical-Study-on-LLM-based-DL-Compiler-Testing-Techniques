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
        self.conv = torch.nn.Conv2d(2, 1, 1, stride=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 - (t / 255))
        return v2




func = Model().to('cuda')




t = torch.tensor([[[0, 255], [0, 255]], [[255, 0], [255, 0]]], dtype=torch.uint8)




x = torch.zeros([1, 2, 2, 2], dtype=torch.uint8)


test_inputs = [t, x]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''