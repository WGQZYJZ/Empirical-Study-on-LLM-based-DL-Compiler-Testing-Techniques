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
        self.conv_transpose = torch.nn.ConvTranspose2d(16384, 16384, 3, stride=1, padding=1, bias=False)
        self.avgpool = torch.nn.AdaptiveAvgPool2d(5, 5)

    def forward(self, x):
        v1 = self.conv_transpose(x)
        v2 = self.avgpool(v1)
        v3 = torch.flatten(v2, 1)
        v4 = torch.tanh(v3)
        return v4




func = Model().to('cuda')



x = torch.randn(64, 16384, 1, 1)


test_inputs = [x]
