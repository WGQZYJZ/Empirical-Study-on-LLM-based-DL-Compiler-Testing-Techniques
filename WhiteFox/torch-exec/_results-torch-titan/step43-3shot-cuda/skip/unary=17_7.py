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
        self.conv = torch.nn.ConvTranspose1d(in_channels=20, out_channels=128, kernel_size=3, activation='relu')

    def forward(self, x1):
        x1 = x1.flip(1).transpose(0, 1)
        v1 = self.conv(x1)
        v2 = v1.transpose(0, 1).flip(1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(20, 30)


test_inputs = [x1]
