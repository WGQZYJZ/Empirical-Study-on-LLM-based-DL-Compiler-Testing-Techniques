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
        self.conv = torch.nn.Conv2d(1, 3000, 32, stride=1)
        self.tanh = torch.nn.Tanh()
        self.conv1 = torch.nn.Conv2d(3000, 3000, 4, stride=1)

    def forward(self, x):
        x = self.conv(x)
        x = self.tanh(x)
        x = self.conv1(x)
        x = self.tanh(x)
    return x



func = ModelTanh().to('cpu')


x = torch.randn(1, 1, 64, 32)

test_inputs = [x]
