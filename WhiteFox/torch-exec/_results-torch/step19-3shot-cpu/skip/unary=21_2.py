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
        self.tanh = torch.nn.Tanh()
        self.conv1 = torch.nn.Conv2d(3, 13, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(12, 10, 3, stride=2, padding=1, groups=4)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.tanh(v1)
        return self.conv2(v2)



func = ModelTanh().to('cpu')


x = torch.randn(1, 3, 64, 64)

test_inputs = [x]
