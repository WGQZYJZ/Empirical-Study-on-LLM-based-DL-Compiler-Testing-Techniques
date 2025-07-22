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

    def __init__(self, min_value=(- 0.7), max_value=3):
        super().__init__()
        self.sigmoid = torch.nn.Sigmoid()
        self.clamp = torch.nn.Clamp(min=min_value, max=max_value)
        self.conv_transpose2d = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv_transpose2d(x1)
        v2 = self.clamp(v1)
        v3 = self.sigmoid(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]
