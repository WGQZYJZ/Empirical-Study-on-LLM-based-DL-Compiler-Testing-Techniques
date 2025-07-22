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
        self._conv = torch.nn.Conv2d(in_channels=1, out_channels=1, kernel_size=(1, 2), bias=False)

    def forward(self, x):
        y1 = self._conv(x)
        y2 = y1.detach().numpy()
        y3 = np.tanh(y2)
    return torch.tensor(y3)



func = ModelTanh().to('cpu')


x = torch.randn(1, 1, 2, 2)

test_inputs = [x]
