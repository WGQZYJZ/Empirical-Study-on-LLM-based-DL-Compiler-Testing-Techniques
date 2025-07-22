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
        self.conv = torch.nn.modules.conv.Conv2d(3, 16, 3, stride=1, padding=2)
        self.brelu = torch.nn.modules.activation.BatchNorm2d(num_features=16)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.brelu(v1)
        v3 = self.brelu(v2)
        v4 = self.brelu(v3)
        return v4



func = Model().to('cpu')


x1 = torch.randn(5, 1, 100, 100)

test_inputs = [x1]
