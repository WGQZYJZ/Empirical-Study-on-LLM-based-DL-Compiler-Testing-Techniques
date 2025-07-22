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
        self.conv = torch.nn.Conv2d(3, 3, 3, groups=2)
        self.bn = torch.nn.BatchNorm2d(3)

    def forward(self, x4):
        x4 = self.bn(self.conv(x4))
        return x4



func = Model().to('cpu')


x4 = torch.randn(1, 6, 4, 4)

test_inputs = [x4]
