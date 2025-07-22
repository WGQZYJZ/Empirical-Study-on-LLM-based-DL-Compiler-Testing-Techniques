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
        self.conv1 = torch.nn.Conv2d(3, 32, 3, stride=1, padding=(2, 1))
        self.conv2 = self.conv1.conv2d

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.add(v2, 5)
        v4 = torch.clamp(v3, 0, 6)
        v5 = (v4 * 3)
        v6 = (v4 / 6)
        return v6.unsqueeze((- 1))




func = Model().to('cuda')



x1 = torch.randn(3, 3, 128, 128)


test_inputs = [x1]
