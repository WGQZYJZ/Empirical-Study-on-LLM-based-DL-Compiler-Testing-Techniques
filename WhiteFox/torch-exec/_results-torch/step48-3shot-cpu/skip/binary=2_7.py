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
        self.conv = torch.nn.Conv2d(1, 32, 3, stride=1, padding=3, dilation=2, groups=32)

    def forward(self, x2):
        v1 = self.conv(x2)
        v2 = v1 - 0.000358
        v3 = v2 - 3.58e-06
        v4 = v3 - 3.583286e-06
        v5 = v4 - 3.58328675e-06
        return v5



func = Model().to('cpu')


x2 = torch.randn(1, 1, 30, 30)

test_inputs = [x2]
