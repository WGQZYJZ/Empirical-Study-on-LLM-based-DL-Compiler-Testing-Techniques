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
        self.conv_transpose = torch.nn.ConvTranspose2d(1, 16, kernel_size=1, stride=5)
        self.relu = torch.relu()

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.relu(v1)
        v3 = self.conv_transpose(v2)
        v4 = self.relu(v3)
        v5 = self.conv_transpose(v4)
        v6 = torch.tanh(v5)
        return v6



func = Model().to('cpu')


x1 = torch.randn(1, 1, 1, 1)

test_inputs = [x1]
