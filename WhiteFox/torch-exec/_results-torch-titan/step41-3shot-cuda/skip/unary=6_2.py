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
        self.conv = torch.nn.Conv2d(3, 3, 1, stride=1, padding=1)
        self.soft_tanh = torch.nn.Softtanh()

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = (3 + t1)
        t3 = torch.clamp(t2, 0, 6)
        t4 = (t1 * t3)
        t5 = (t4 / 6)
        t6 = self.soft_tanh(t5)
        return t6




func = Model().to('cuda')



x1 = torch.randn(2, 3, 64, 64)


test_inputs = [x1]
