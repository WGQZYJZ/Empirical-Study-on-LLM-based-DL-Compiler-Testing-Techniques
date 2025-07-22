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
        self.conv = torch.nn.Conv2d(64, 128, (7, 6), stride=2, padding=(0, 2))

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = F.relu(v1)
        return v2



func = Model().to('cuda')


x1 = torch.randn(1, 64, 128, 64)

test_inputs = [x1]
