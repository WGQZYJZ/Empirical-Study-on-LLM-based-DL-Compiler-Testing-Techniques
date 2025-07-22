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



class Module(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(226, 224, 5, bias=False)
        self.transpose = torch.nn.functional.interpolate(size=(2, 2), scale_factor=None, mode='bilinear', align_corners=False)

    def forward(self, x4):
        m1 = self.conv_t(x4)
        m2 = (m1 > 0)
        m3 = (m1 * 0.968709)
        m4 = torch.where(m2, m1, m3)
        out = self.transpose(m4)
        return out




class Module(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(39, 38, 7, stride=9, padding=0, output_padding=0, groups=39, bias=False)
        self.transpose = torch.nn.functional.interpolate(size=203, scale_factor=46, mode='bilinear', align_corners=False)

    def forward(self, x1):
        m1 = self.conv_t(x1)
        m2 = (m1 > 0)
        m3 = (m1 * (- 0.24230232))
        m4 = torch.where(m2, m1, m3)
        out = self.transpose(m4)
        return out




func = Module().to('cuda')



x4 = torch.randn(5, 226, 59, 55)



x1 = torch.randn(31, 39, 1, 3)


test_inputs = [x4, x1]
