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
        self.conv = torch.nn.Conv2d(19, 1, padding=3)
        self.conv1 = torch.nn.Conv2d(19, 49, padding=5)
        self.conv2 = torch.nn.Conv2d(49, 19, padding=7)
        self.conv3 = torch.nn.Conv2d(19, 1, padding=9)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.conv1(v1)
        v3 = self.conv2(v2)
        v4 = torch.tanh(v3)
        v5 = self.conv3(v4)
        return v5




func = ModelTanh().to('cuda')



x = torch.randn(50, 19, 48, 70)


test_inputs = [x]
