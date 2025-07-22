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
        self.conv = torch.nn.Conv2d(1, 3, 5, stride=1, padding=0, dilation=1, groups=3, bias=False)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 - 0.09766342)
        return v2




func = Model().to('cuda')



x = torch.randn(1, 1, 112, 112)


test_inputs = [x]
