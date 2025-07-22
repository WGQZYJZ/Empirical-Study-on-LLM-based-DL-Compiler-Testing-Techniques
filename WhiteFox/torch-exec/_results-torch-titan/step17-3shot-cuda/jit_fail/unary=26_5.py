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



class M1(torch.nn.Module):

    def __init__(self, in_channels, out_channels, kernel_size, stride, padding, bias, dilation):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(in_channels, out_channels, kernel_size, stride, padding, bias=bias, dilation=dilation)

    def forward(self, x2):
        f1 = self.conv_t(x2)
        f2 = torch.relu(f1)
        return f2




class M2(torch.nn.Module):

    def __init__(self, in_channels, out_channels, kernel_size, stride, padding):
        super().__init__()
        self.conv_t1 = torch.nn.ConvTranspose2d(in_channels, out_channels, kernel_size, stride, padding, bias=False)
        self.bn1 = torch.nn.BatchNorm2d(out_channels)
        self.relu1 = torch.nn.ReLU()

    def forward(self, x1):
        t2 = self.conv_t1(x1)
        f1 = self.bn1(t2)
        g1 = self.relu1(f1)
        return g1




class M3(torch.nn.Module):

    def __init__(self, in_channels, out_channels, kernel_size, stride, padding):
        super().__init__()
        self.conv_t1 = torch.nn.ConvTranspose2d(in_channels, out_channels, kernel_size, stride, padding, bias=False)
        self.relu1 = torch.nn.ReLU()

    def forward(self, x):
        x1 = self.conv_t1(x)
        x2 = self.relu1(x1)
        return x2



in_channels = 1
out_channels = 1
kernel_size = 1
stride = 1
padding = 1

func = M3(in_channels, out_channels, kernel_size, stride, padding).to('cuda')



x2 = torch.randn(1, 100, 8, 8)



x1 = torch.randn(1, 50, 8, 8)


test_inputs = [x2, x1]

# JIT_FAIL
'''
direct:
forward() takes 2 positional arguments but 3 were given

jit:
forward() takes 2 positional arguments but 3 were given
'''