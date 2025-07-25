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
        self.modulelist = torch.nn.ModuleList([torch.nn.Conv2d(2, 1, 4, stride=2, padding=2), torch.nn.Conv2d(4, 2, 4, stride=1, padding=2)])
        self.add = torch.nn.Add()
        self.conv = torch.nn.Conv2d(2, 1, 3, stride=1, padding=2)

    def forward(self, x):
        v1 = self.modulelist[0](x)
        v2 = self.modulelist[1](v1)
        v3 = self.add(v1, v2)
        return self.conv(v3)



func = Model().to('cpu')


x = torch.randn(1, 2, 32, 32)

test_inputs = [x]
