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
        self.linear = torch.nn.linear(3, 8)

    def forward(self, x1, other):
        v1 = self.linear(x)
        v2 = (v1 + other)
        return v2



func = Model().to('cuda')



x1 = torch.randn(1, 3)

other = 1

test_inputs = [x1, other]
