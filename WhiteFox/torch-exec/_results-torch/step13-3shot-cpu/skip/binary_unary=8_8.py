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
        self.conv1 = torch.nn.Conv2d(3, 8, 1, padding=1, groups=2)
        self.conv2 = torch.nn.Conv2d(3, 8, 1, padding=1, groups=2)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(x1)
        t1 = v1 + v1
        v3 = torch.relu(t1)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 3, 64, 64)

test_inputs = [x1]
