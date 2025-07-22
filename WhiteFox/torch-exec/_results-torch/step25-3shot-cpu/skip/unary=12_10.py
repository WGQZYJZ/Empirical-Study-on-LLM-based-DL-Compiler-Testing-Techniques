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
        self.conv1 = torch.nn.Conv2d(17, 17, 15, stride=1, padding=0, dilation=13, groups=17)
        self.conv2 = torch.nn.Conv2d(17, 32, 1, stride=1, padding=0, dilation=1, groups=17)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v1.sigmoid()
        v2 = self.conv2(x1)
        v2.sigmoid()
        return torch.cat((v1, v2), 0)



func = Model().to('cpu')


x1 = torch.randn(1, 17, 64, 64)

test_inputs = [x1]
