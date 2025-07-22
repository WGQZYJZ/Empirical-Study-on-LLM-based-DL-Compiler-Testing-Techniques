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
        self.conv = torch.nn.Conv2d(in_channels=1, out_channels=2, kernel_size=(2, 2), stride=(2, 2), bias=None)
        weight = torch.randn(2, 1, 2, 2, device='cuda')
        self.conv = torch.nn.Conv2d(in_channels=1, out_channels=2, kernel_size=(2, 2), stride=(2, 2), bias=None).cuda().weight.data = weight

    def forward(self, x1):
        v0 = self.conv(x1)
        return v0



func = Model().to('cpu')

x1 = 1

test_inputs = [x1]
