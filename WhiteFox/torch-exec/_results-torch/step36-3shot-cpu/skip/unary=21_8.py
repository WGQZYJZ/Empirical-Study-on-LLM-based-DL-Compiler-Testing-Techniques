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
        self.conv = torch.nn.Conv1d(2, 1, 2, groups=2, bias=False)

    def forward(self, x):
        v3 = self.conv(x)
        v4 = torch.tanh(v3)
        return v4



func = ModelTanh().to('cpu')


x = torch.randn(1, 2, 13)

test_inputs = [x]
