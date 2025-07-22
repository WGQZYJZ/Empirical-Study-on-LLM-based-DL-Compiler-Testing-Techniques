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
        self.conv_t = torch.nn.ConvTranspose2d(7, 11, 6, stride=2, padding=2, groups=7)

    def forward(self, x):
        x1 = self.conv_t(x)
        x2 = x1 > 0
        x3 = x1 * -0.94
        x4 = torch.where(x2, x1, x3)
        return x4



func = Model().to('cpu')


x = torch.randn(15, 7, 16, 12)

test_inputs = [x]
