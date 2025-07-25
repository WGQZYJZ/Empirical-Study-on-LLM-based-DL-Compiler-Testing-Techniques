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
        self.conv = torch.nn.Conv2d(2, 3, 1, stride=1, padding=1)
        self.conv = torch.nn.functional.avg_pool2d(self.conv, 2, stride=2, padding=0)

    def forward(self, x1):
        t1 = self.conv(x1)
        t2 = (t1 + 3)
        t3 = torch.clamp_min(t2, 0)
        t4 = torch.clamp_max(t3, 6)
        t5 = (t1 * t4)
        t6 = (t5 / 6)
        return t6




func = Model().to('cuda')



x1 = torch.randn(1, 2, 128, 128)


test_inputs = [x1]
