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
        self.conv_transpose = torch.nn.ConvTranspose2d(in_channels=7, kernel_size=(5, 5), out_channels=7)
        self.act_7 = torch.nn.ELU()
        self.min_value = min_value

    def forward(self, x):
        v4 = self.conv_transpose(x)
        v5 = torch.clamp_min(v4, self.min_value)
        v6 = torch.clamp_max(v5, max_value)
        v7 = self.act_7(v6)
        return v7



func = Model().to('cpu')


x6 = torch.randn(1, 7, 128, 128)

test_inputs = [x6]
