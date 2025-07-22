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
        self.linear = MyLinear()

    def forward(self, x, other=None):
        if other is None:
            other = torch.randn_like(x)
        v1 = self.linear(x)
        v2 = v1 + other
        return v2


func = Model().to('cuda')


x = torch.randn(1, 16)

test_inputs = [x]
