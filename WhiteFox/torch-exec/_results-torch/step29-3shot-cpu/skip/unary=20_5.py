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
        self.conv_t = torch.nn.ConvTranspose2d(3, 16, kernel_size=3, stride=1, padding=1, output_padding=1, groups=3)
        self.bn = torch.nn.BatchNorm1d(16)
        self.maxpool_t = torch.nn.MaxPool2d(3, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.bn(self.conv_t(x1))
        v2 = self.maxpool_t(torch.tanh(v1))
        return torch.tanh(v2)



func = Model().to('cpu')


x1 = torch.randn(1, 3, 608, 358)

test_inputs = [x1]
