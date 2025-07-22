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

    def __init__(self, min_value=1.41421):
        super().__init__()
        self.relu6 = torch.nn.ReLU6(min_value=min_value)
        self.conv = torch.nn.Conv2d(5, 7, 2, stride=1)

    def forward(self, x1):
        v1 = self.relu6(x1)
        v2 = self.conv(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 5, 152, 152)

test_inputs = [x1]
