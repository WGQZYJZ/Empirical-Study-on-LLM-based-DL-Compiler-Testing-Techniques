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
        self.conv = torch.nn.Conv2d(3, 2, 3, stride=1, padding=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(2, 3, 3, stride=1, padding=1, groups=2)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.tanh(v1)
        v3 = self.conv_transpose(v2)
        return v3




func = Model().to('cuda')



x1 = torch.randn(1, 3, 3, 3)


test_inputs = [x1]
