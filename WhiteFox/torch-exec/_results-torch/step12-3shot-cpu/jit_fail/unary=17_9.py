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
        self.conv1 = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = self.sigmoid(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 3, 224, 224)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'sigmoid'

jit:
'Model' object has no attribute 'sigmoid'
'''