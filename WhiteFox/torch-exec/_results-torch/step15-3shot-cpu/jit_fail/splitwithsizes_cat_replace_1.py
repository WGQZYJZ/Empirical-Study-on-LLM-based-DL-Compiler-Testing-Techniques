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
        self.features = torch.nn.Sequential(torch.nn.Conv2d(3, 32, 3, 1, 1), torch.nn.Conv2d(32, 32, 1, 1, 0), torch.nn.Conv2d(32, 3, 3, 1, 1))
        self.split1 = torch.nn.Sequential(torch.nn.Conv2d(3, 32, 1, 1, 0))
        self.split2 = torch.nn.Sequential(torch.nn.Conv2d(3, 16, 3, 1, 1))

    def forward(self, x1):
        v1 = self.features(x1)
        split_tensors1 = torch.split(v1, [1, 1, 1], dim=1)
        split_tensors2 = torch.split(v1, [1, 1, 1], dim=1)
        self.save_for_backward(torch.cat(split_tensors1, dim=1))
        return (torch.cat(split_tensors2, dim=1), torch.split(v1, [1, 1, 1], dim=1))



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'save_for_backward'

jit:
'Model' object has no attribute 'save_for_backward'
'''