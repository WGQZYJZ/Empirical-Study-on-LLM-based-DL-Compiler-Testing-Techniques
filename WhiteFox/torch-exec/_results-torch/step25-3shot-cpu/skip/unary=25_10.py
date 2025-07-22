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

    def __init__(self, negative_slope):
        super().__init__()
        self.negative_slope = negative_slope
        self.linear = torch.nn.Linear(1, 1, bias=False)

    def forward(self, input):
        z = self.linear(input)
        return torch.where(z > 0, z, self.negative_slope * z).view(1, 1)


negative_slope = 1
func = Model(s).to('cpu')


x = torch.randn(1, 1)

test_inputs = [x]
