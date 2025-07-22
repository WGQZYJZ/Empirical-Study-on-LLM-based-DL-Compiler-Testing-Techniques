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
        self.conv = torch.nn.Conv2d(3, 1, 7, stride=1, padding=0, dilation=1, groups=2)
        self.tanh = torch.nn.Tanh()

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.tanh(v1)
        return v2




func = ModelTanh().to('cuda')



x = torch.randn(1, 3, 32, 32)


test_inputs = [x]
