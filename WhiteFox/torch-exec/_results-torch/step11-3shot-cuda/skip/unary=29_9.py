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

    def __init__(self, min_value=0.5, max_value=0.2):
        super().init()
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 1, 1, stride=1, padding=0, bias=False)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        x2 = self.conv_transpose(x1)
        x3 = torch.clamp_min(x2, self.min_value)
        x4 = torch.clamp_max(x3, -self.max_value)
        x5 = self.min_value * x4



func = Model().to('cuda')


x1 = torch.randn(1, 16, 256, 256)

test_inputs = [x1]
