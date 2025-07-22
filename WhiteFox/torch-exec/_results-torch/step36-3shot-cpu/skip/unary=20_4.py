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

class Model(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = nn.ConvTranspose2d(1, 1, stride=2, padding=10, bias=False)
        self.bn = nn.BatchNorm2d(1, momentum=0.0001, affine=True)
        self.relu = nn.LeakyReLU(inplace=False)

    def forward(self, x1):
        x2 = self.conv1(x1)
        x3 = self.bn(x2)
        x4 = self.relu(x3)
        return x4



func = Model().to('cpu')


x1 = torch.randn(1, 1, 50, 200)

test_inputs = [x1]
