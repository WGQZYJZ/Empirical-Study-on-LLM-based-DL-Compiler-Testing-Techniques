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
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0, groups=2)

    def forward(self, x):
        v1 = self.conv(x)
        v2 = (v1 - 42)
        return v2




func = Model().to('cuda')



x = torch.randn(1, 6, 64, 64)


test_inputs = [x]
