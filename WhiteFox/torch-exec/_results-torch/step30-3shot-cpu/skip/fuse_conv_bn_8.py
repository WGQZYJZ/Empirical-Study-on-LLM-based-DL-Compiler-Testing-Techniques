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
        self.conv1 = torch.nn.Conv2d(3, 3, 3)
        self.conv2 = torch.nn.Conv2d(3, 3, 3)
        self.bn = torch.nn.BatchNorm2d(3, running_mean=torch.arange(3, dtype=torch.float), running_var=torch.arange(3, dtype=torch.float) * 2 + 1)

    def forward(self, x1, x2):
        s = self.conv1(x1)
        t = self.conv2(s)
        y = self.bn(t)
        return s



func = Model().to('cpu')


x1 = torch.randn(1, 3, 6, 6)

x2 = torch.randn(1, 3, 6, 6)

test_inputs = [x1, x2]
