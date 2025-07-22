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
        self.conv1 = torch.nn.Conv2d([1, 144, 48, 76], 1, kernel_size=(1, 64), stride=(1, 1), padding=(0, 0))
        self.conv2 = torch.nn.Conv2d([1, 144, 48, 76], 1, kernel_size=(1, 64), stride=(1, 1), padding=(0, 0))

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = v2 - 3.46
        return v3



func = Model().to('cpu')


x = torch.randn(1, 1, 346, 1985)

test_inputs = [x]
