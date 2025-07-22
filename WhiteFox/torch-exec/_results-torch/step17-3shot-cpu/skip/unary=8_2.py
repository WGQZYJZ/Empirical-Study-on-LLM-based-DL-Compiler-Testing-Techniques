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
        self.conv_transpose1 = torch.nn.ConvTranspose2d(10, 50, 5, groups=10)
        self.conv_transpose2 = torch.nn.ConvTranspose2d(25, 64, 5, groups=5, stride=4)
        self.conv_transpose3 = torch.nn.ConvTranspose2d(45, 83, 7, groups=25, stride=4)

    def forward(self, x1):
        v1 = self.conv_transpose1(x1)
        v2 = self.conv_transpose2(v1)
        v3 = self.conv_transpose3(v2)
        v4 = v3 / 100
        return v4



func = Model().to('cpu')


x1 = torch.randn(1, 10, 37, 30)

test_inputs = [x1]
