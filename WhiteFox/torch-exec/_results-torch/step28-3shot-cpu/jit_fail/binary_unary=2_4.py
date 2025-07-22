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

class MyModel(nn.Module):

    def __init__(self):
        super(MyModel, self).__init__()
        self.con1 = nn.Conv2d(3, 3, 3, stride=2, padding=1)
        self.conv2 = nn.Conv2d(3, 3, 3, stride=2, padding=1)
        self.conv3 = nn.Conv2d(3, 3, 3, stride=2, padding=1)
        self.conv4 = nn.Conv2d(3, 3, 1, stride=1, padding=0)

    def forward(self, x):
        y = self.conv1(x - 0.3)
        y = self.conv2(y - 1.0)
        y = self.conv3(y - 2.0)
        y = self.conv4(y - 2.5)
        return y



func = MyModel().to('cpu')


x1 = torch.randn(1, 3, 32, 32)

test_inputs = [x1]

# JIT_FAIL
'''
direct:
'MyModel' object has no attribute 'conv1'

jit:
'MyModel' object has no attribute 'conv1'
'''