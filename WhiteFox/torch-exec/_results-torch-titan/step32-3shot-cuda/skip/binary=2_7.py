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
        self.conv = torch.nn.Conv2d(3, 4, 1, stride=1, padding=0, dilation=2, groups=2)

    def forward(self, x4):
        v1 = self.conv(x4)
        v2 = (v1 - False)
        return v2




func = Model().to('cuda')



x4 = torch.randn(1, 3, 2, 2)


test_inputs = [x4]
