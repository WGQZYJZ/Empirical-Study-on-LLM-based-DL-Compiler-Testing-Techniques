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

    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 3, 3, dilation=1, groups=16)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.sigmoid(v1)
        v3 = (v1 * v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 16, 64, 64)


test_inputs = [x1]
