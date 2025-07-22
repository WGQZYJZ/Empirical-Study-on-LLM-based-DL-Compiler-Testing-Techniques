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
        self.conv = torch.nn.Conv2d(1, 12, 1, stride=1, transposed=True)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - 1.0
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 1, 1, 1)

test_inputs = [x1]
