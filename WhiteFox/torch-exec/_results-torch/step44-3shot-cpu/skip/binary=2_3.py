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
        self.conv = torch.nn.Conv3d(5, 16, 5, stride=2, padding=0, output_padding=0, dilation=1, groups=2, bias=1)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - 1.72
        return v2



func = Model().to('cpu')


x = torch.randn(1, 5, 16, 32, 32)

test_inputs = [x]
