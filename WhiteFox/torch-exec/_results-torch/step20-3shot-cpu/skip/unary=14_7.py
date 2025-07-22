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
        self.conv_d_s_r = torch.nn.Sequential(torch.nn.Conv2d(64, 64, 3, stride=1, padding=0), torch.nn.Dropout(p=0.3), torch.nn.Sigmoid(), torch.nn.Conv2d(64, 64, 4, stride=2, padding=1, output_padding=0))

    def forward(self, x1):
        v1 = self.conv_d_s_r(x1)
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 64, 32, 32)

test_inputs = [x1]
