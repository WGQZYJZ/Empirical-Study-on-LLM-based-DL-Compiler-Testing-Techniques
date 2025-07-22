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
        self.conv = torch.nn.Conv2d(3, 32, 5, stride=1, padding=2, groups=3)
        self.conv1 = torch.nn.Conv2d(1, 8, 1, stride=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv1(x1)
        v3 = (v1 - v2)
        v4 = F.relu(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 3, 256, 256)


test_inputs = [x1]
