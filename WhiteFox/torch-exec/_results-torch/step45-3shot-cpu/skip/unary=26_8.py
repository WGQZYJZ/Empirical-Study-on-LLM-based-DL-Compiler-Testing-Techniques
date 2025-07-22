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
        self.conv_t = torch.nn.ConvTranspose1d(93, 100, stride=3, bias=False, padding=1)

    def forward(self, x):
        m1 = self.conv_t(x)
        m2 = m1 > 0
        m3 = m1 * -8.48
        m4 = torch.where(m1 > 2.5, m1, m3)
        m5 = torch.where(m2, m1, m4)
        return m5



func = Model().to('cpu')


x = torch.randn(23, 93)

test_inputs = [x]
