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
        self.m = torch.nn.Sequential(torch.nn.Conv2d(in_channels=3, out_channels=1, kernel_size=3, stride=1, padding=1, dilation=1, groups=1, bias=True, padding_mode='zero'), torch.nn.Sigmoid())

    def forward(self, x1):
        v1 = self.m(x1)
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 3, 32, 32)

test_inputs = [x1]
