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
        self.conv = torch.nn.Conv2d(7, 12, 3, stride=1, padding=0)
        self.conv_transpose = torch.nn.ConvTranspose2d(12, 10, 5, stride=4, padding=3, output_padding=2, groups=3)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.conv_transpose(v1)
        v3 = torch.relu(v2)
        return v3



func = Model().to('cpu')


x1 = torch.randn(1, 7, 20, 20)

test_inputs = [x1]
