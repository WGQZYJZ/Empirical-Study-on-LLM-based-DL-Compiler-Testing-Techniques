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

    def forward(self, x1):
        o0 = self.conv1(x1)
        o1 = self.bn1(o0)
        o2 = torch.tanh(o1)
        o3 = self.conv2(o2)
        o4 = self.bn2(o3)
        o5 = torch.tanh(o4)
        o6 = self.conv2(o5)
        o7 = self.bn2(o6)
        o8 = torch.tanh(o7)
        o9 = self.pooling2d_2(o8)
        oa = o9.squeeze_(-1).squeeze_(-1)
        ob = self.dense1(oa)
        oc = self.dense2(ob)
        return oc


func = Model().to('cpu')


x1 = torch.randn(1, 3, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'Model' object has no attribute 'conv1'

jit:
'Model' object has no attribute 'conv1'
'''