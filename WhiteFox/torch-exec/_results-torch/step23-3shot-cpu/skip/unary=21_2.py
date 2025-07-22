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

class ModelTanh(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(64, 256, 1, stride=1, padding=0, stride=1, dilation=1, groups=1, bias=True)
        self.tanh = torch.nn.Tanh()

    def forward(self, x2):
        x2 = self.conv(x2)
        v1 = self.tanh(x2)
        return v1



func = ModelTanh().to('cpu')


x2 = torch.randn(1024, 64, 8, 8)

test_inputs = [x2]
