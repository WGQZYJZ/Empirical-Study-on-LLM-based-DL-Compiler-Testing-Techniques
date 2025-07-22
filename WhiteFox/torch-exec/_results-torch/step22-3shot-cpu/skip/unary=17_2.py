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
        self.conv_transpose = torch.nn.ConvTranspose3d(2, 128, [2, 2, 2], stride=[1, 1, 1], padding=[0, 0, 0], groups=4)

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 2, 50, 30, 30)

test_inputs = [x1]
