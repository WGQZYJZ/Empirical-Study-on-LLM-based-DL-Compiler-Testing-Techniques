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
        x1 = torch.randn(4, 5, 1, 1) - 3
        self.weight = torch.nn.Parameter(x1.expand((64, 5, 3, 3)))
        self.conv_transpose = torch.nn.ConvTranspose2d(5, 8, 1, stride=3, output_padding=1)

    def forward(self, x2):
        v1 = self.conv_transpose(x2, self.weight)
        v2 = v1 + 3
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = v1 * v4
        v6 = v5 / 6
        return v6



func = Model().to('cpu')


x2 = torch.randn(1, 5, 32, 32)

test_inputs = [x2]
