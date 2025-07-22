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
        self.conv = torch.nn.Conv2d(1, 4, 3, padding=100, groups=3)
        self.tanh = torch.nn.Tanh()

    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.tanh(v1)
        return v2



func = ModelTanh().to('cpu')


x = torch.randn(1, 1, 10, 4)

test_inputs = [x]
