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

class ModelTanh(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2D(1, 1, 1)
        self.tanh = nn.Tanh()

    def forward(self, x1):
        x2 = self.conv1(x1)
        y2 = self.tanh(x2)
        return y2



func = ModelTanh().to('cpu')


x1 = torch.randn(1, 1, 3, 3)

test_inputs = [x1]
