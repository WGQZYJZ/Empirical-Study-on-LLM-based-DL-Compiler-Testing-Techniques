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
        self.conv = torch.nn.Conv2d(1, 8, 3, 1, 2, 2, 2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv(x1)
        v3 = (v1 + v2)
        v4 = torch.relu(v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(1, 1, 64, 64)


test_inputs = [x1]
