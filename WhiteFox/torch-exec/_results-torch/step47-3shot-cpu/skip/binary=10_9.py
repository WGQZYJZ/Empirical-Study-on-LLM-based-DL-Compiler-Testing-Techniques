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

class Model1(torch.nn.Module):

    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(4, 5)
        self.other = torch.nn.Parameter(other)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        return v2


other = 1

func = Model1(other).to('cpu')

x1 = 1

test_inputs = [x1]
