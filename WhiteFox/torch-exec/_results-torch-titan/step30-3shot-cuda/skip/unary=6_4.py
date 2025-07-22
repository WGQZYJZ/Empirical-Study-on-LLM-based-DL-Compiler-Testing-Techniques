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
        self.conv = torch.nn.Conv2d(3, 1, 7, stride=2, padding=1, groups=3)
        self.bn = torch.nn.BatchNorm2d(1)

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = self.bn(t1)
        t3 = (t2 + 3)
        t4 = F.hardtanh(t3, min_val=(- 4.0), max_val=6.0)
        t5 = (t2 * t4)
        t6 = (t5 / 6)
        return t6




func = Model().to('cuda')



x1 = torch.randn(1, 3, 56, 56)


test_inputs = [x1]
