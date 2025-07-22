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
        self.conv_transpose = torch.nn.ConvTranspose1d(424, 254, kernel_size=2, stride=3, padding=3, groups=22, dilation=0, bias=False)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.sigmoid(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(22, 424, 8)

test_inputs = [x1]
