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
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=7, kernel_size=(1, 1), stride=(1, 1), padding=0)
        self.conv2 = torch.nn.Conv2d(in_channels=7, out_channels=3, kernel_size=(3, 3), stride=(2, 3), padding=1)
        self.conv3 = torch.nn.Conv2d(in_channels=3, out_channels=10, kernel_size=(2, 2), stride=(1, 1), padding=0)
        self.conv4 = torch.nn.Conv2d(in_channels=10, out_channels=6, kernel_size=(5, 5), stride=(2, 2), padding=1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = torch.sigmoid(v1)
        v3 = self.conv2(v2)
        v4 = self.conv3(v3)
        v5 = torch.sigmoid(v4)
        v6 = self.conv4(v5)
        v7 = torch.sigmoid(v6)
        return v7




func = Model().to('cuda')



x1 = torch.rand(7, 3, 64, 64)



x2 = torch.randn(1, 3, 64, 64)



x3 = torch.rand(9, 3, 32, 32)



x4 = torch.randn(4, 3, 32, 32)


test_inputs = [x1, x2, x3, x4]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 5 were given

jit:
forward() takes 2 positional arguments but 5 were given
'''