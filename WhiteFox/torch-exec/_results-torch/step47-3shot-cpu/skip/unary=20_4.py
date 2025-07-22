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
        self.conv_transp = torch.nn.ConvTranspose1d(9, 8, 3, stride=1, padding=0, groups=3, bias=False, dilation=2)

    def forward(self, x1):
        v1 = self.conv_transp(x1)
        v2 = torch.sigmoid(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 9, 16)

test_inputs = [x1]
