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
        self.conv = torch.nn.Conv2d([1, 3, 6], 3, [3, 5], 1, padding=[1, 2])

    def forward(self, x1):
        v1 = self.conv(x1)
        return v1



func = Model().to('cpu')


x1 = torch.randn(1, 1, 10, 10)

test_inputs = [x1]
