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

    def __init__(self, min, max):
        super().__init__()
        self.q = torch.nn.quantized_relu(torch.nn.Conv2d(3, 1, 1, stride=1, padding=0))
        self.min = min
        self.max = max

    def forward(self, x1):
        x2 = self.q(x1)
        x3 = torch.nn.functional.relu(x2, self.min, self.max)
        return x3


min = 0.85
max = 0.98

func = Model(min, max).to('cpu')


x1 = torch.randn(3, 3, 32, 32)

test_inputs = [x1]
