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
        self.conv = torch.nn.Conv2d(1, 6, kernel_size=(1, 1), stride=(1, 1), padding=(0, 0), dilation=(1, 1), groups=6, bias=False)
        self.linear = torch.nn.Linear(3072, 512)

    def forward(self, x1):
        v1 = self.conv(x1)
        v1 = F.relu(v1)
        v1 = self.linear(v1)
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 1, 224, 224)

test_inputs = [x1]
