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

    def __init__(self, in_channels, out_channels, bias_channel):
        super(Model, self).__init__()
        self.conv_t = torch.nn.ConvTranspose2d(in_channels, out_channels, kernel_size=4, stride=2, padding=1, bias=bias_channel, groups=1)
        if bias_channel:
            self.conv.bias.requires_grad = False
            self.conv_t.bias = None

    def forward(self, x3):
        z1 = self.conv_t(x3)
        z2 = (z1 > 0)
        z3 = (z1 * (- 0.731))
        z4 = torch.where(z2, z1, z3)
        return torch.nn.functional.avg_pool2d(z4, kernel_size=(4, 4))



in_channels = 1
out_channels = 1
bias_channel = 1

func = Model(in_channels, out_channels, bias_channel).to('cuda')



x3 = torch.randn(1, 1, 4, 5)


test_inputs = [x3]
