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
        self.conv_transpose = torch.nn.ConvTranspose2d(in_channels=16, kernel_size=3, out_channels=29, stride=(1, 26), dilation=(50, 65), padding=(60, 77), groups=6, bias=True, padding_mode='zeros')

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = x92(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 16, 558, 507)

test_inputs = [x1]
