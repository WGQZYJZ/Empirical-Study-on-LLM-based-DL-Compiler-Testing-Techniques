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
        self._conv1 = torch.nn.ConvTranspose2d((64,), (32,), (1, 1), (1, 1), 0, bias=False)

    def forward(self, x):
        v = self._conv1(x)
        return v



func = Model().to('cpu')


x = torch.randn(1, 64, 112, 112)

test_inputs = [x]
