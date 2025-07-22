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
        super(Model).__init__()
        self.conv = torch.nn.Conv2d(2, 4, 3, stride=2, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 2.0
        return v2



func = Model().to('cpu')


x1 = torch.randn(1, 2, 35, 35)

test_inputs = [x1]
