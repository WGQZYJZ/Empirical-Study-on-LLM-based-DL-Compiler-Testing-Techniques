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
        msd_layers = []
        msd_layers += [torch.nn.MaxPool2d(3, stride=2, padding=1), torch.nn.Conv2d(1, 3, 3, stride=2, groups=3), torch.nn.Conv2d(3, 1, 1, stride=1, groups=3)]
        msd_layers[-1].out_channels = 1
        msd_layers += [torch.nn.ReLU(inplace=True)]
        self.msd = torch.nn.Sequential(*msd_layers)
        mfd_layers = []
        mfd_layers += [torch.nn.Conv2d(1, 3, 3, stride=2)]
        mfd_layers[-1].groups = 3
        mfd_layers += [torch.nn.Conv2d(3, 1, 1, stride=1)]
        mfd_layers[-1].groups = 3
        mfd_layers += [torch.nn.ReLU(inplace=True)]
        self.mfd = torch.nn.Sequential(*mfd_layers)
        fre_layers = []
        fre_layers += [torch.nn.Conv2d(1, 1, 1)]
        fre_layers[-1].groups = 1
        fre_layers += [torch.nn.Sigmoid()]
        self.fre = torch.nn.Sequential(*fre_layers)

    def forward(self, x1):
        v1 = self.msd(x1)
        v2 = torch.abs(x1 - v1)
        v3 = torch.abs(self.mfd(v2))
        v4 = torch.abs(self.fre(v3))
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 1, 64, 64)

test_inputs = [x1]
