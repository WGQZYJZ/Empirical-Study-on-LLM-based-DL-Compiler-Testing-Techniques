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
        super(M, self).__init__()

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 1
        v3 = torch.clamp(v2, -1, 1)
        return v3


func = Model().to('cpu')


x1 = torch.randn(1, 5)

test_inputs = [x1]
