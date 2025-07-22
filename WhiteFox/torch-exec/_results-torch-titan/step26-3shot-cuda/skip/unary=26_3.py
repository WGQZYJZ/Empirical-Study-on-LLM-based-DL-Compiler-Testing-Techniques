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
        self.conv_t = torch.nn.ConvTranspose2d(1, 12, 7, stride=3, padding=1, dilation=2, groups=12)

    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = (v1 > 0)
        v3 = (v1 * 0.12)
        v4 = torch.where(v2, v1, v3)
        return v4




func = Model().to('cuda')



x1 = torch.randn(20, 1, 28, 28)


test_inputs = [x1]
