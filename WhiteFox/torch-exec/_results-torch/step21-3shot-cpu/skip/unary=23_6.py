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
        self.conv_transpose1d = torch.nn.ConvTranspose1d(1, 2, 10, stride=1, padding=1, dilation=2, output_padding=1, groups=1, bias=False, padding_mode='replicate')

    def forward(self, x1):
        v1 = self.conv_transpose1d(x1)
        v2 = torch.tanh(v1)
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 1, 160)

test_inputs = [x1]
