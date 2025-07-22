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
        self.conv1 = torch.nn.Conv2d(3, 20, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(20, 45, 1, stride=1, padding=0)
        self.conv3 = torch.nn.Conv2d(45, 20, 1, stride=1, padding=0)
        self.conv4 = torch.nn.Conv2d(20, 19, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.conv3(v2)
        v4 = self.conv4(v3)
        v5 = torch.nn.Sigmoid(v4)
        return v5




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]

# JIT_STATUS
'''
direct:
Sigmoid.__init__() takes 1 positional argument but 2 were given

jit:

'''