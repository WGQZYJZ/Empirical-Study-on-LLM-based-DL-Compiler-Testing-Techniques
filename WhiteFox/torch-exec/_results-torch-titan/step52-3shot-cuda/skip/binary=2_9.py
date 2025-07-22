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
        self.w = torch.nn.Parameter(torch.ones((64, 3)))
        self.conv = torch.nn.Conv2d(3, 16, conv, stride=1, padding=1)

    def forward(self, x):
        v = self.conv(x)
        a = 4.2
        b = (a - self.w[(0, ...)])
        v = b.clamp(2.0, 7.2)
        return v




func = Model().to('cuda')



x = torch.randn(3, 64, 31, 63)


test_inputs = [x]
