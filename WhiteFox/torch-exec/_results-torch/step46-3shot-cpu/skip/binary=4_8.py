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
        __self.linear1__ = torch.nn.Linear(3, 12)
        __self.linear2__ = torch.nn.Linear(12, 16)

    def forward(self, x1):
        v1 = self.linear1_(x1)
        v2 = self.linear2_(v1)
        v3 = v2 + other
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 3, 10)

other = torch.randn(1, 16, 10)

test_inputs = [x1, other]
