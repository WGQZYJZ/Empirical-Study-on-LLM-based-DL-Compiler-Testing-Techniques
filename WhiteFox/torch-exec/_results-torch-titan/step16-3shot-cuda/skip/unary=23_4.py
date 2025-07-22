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
        self.conv_transpose_2 = torch.nn.ConvTranspose2d(128, 128, bias=False, groups=6, kernel_size=1, stride=2)

    def forward(self, x1):
        v1 = self.conv_transpose_2(x1)
        v2 = torch.tanh(v1)
        return v2




func = Model().to('cuda')



x1 = torch.randn(1, 128, 16, 16)


test_inputs = [x1]
