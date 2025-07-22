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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(1, 3, 1)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(1, 2, 3, padding=1, groups=3)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(3, 1, 5, stride=1, padding=2, dilation=2)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = self.conv_transpose2(v1)
        v3 = self.conv_transpose3(v2)
        v4 = (v3 + 3)
        v5 = torch.clamp(v4, min=0)
        v6 = torch.clamp(v5, max=6)
        v7 = (v3 * v6)
        v8 = (v7 / 6)
        return v8




func = Model().to('cuda')



x1 = torch.randn(1, 1, 129, 256)


test_inputs = [x1]
