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
        self.conv_t = torch.nn.ConvTranspose2d(1, 1, 4, stride=1, padding=2, groups=3, dilation=1, bias=False)

    def forward(self, x2):
        r1 = self.conv_t(x2)
        r2 = (r1 > 0)
        r3 = (r1 * (- 0.689))
        r4 = torch.where(r2, r1, r3)
        return torch.nn.functional.interpolate(r4, scale_factor=[1.0, 1.0])




func = Model().to('cuda')



x2 = torch.randn(6, 1, 39, 25)


test_inputs = [x2]
