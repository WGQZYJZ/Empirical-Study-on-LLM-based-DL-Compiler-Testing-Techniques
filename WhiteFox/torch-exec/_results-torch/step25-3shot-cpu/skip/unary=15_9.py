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

class Mish(nn.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = x * torch.tanh(nn.functional.softplus(x))
        return x

class Model(nn.Module):

    def __init__(self, in_channel, out_channel, kernelSize=3):
        super(Model, self).__init__()
        self.conv = nn.Conv2d(in_channel, out_channel, kernel_size=kernelSize)
        self.pool = nn.MaxPool2d(kernelSize=2)
        self.dropout = nn.Dropout2d(p=0.25)
        self.mish = Mish()

    def forward(self, x):
        x = self.conv(x)
        x = self.mish(x)
        x = self.pool(x)
        x = self.dropout(x)
        return x


in_channel = 3
out_channel = 8

func = Model(in_channel, out_channel).to('cpu')


in_channel = 3
x1 = torch.randn(1, in_channel, 64, 64)

test_inputs = [x1]
