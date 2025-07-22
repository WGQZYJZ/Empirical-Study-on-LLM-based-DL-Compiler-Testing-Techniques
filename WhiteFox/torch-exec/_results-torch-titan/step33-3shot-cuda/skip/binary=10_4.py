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

    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(256, 512)
        self.other = other

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 + self.other)
        return v2



func = Model(other).to('cuda')



other = torch.randn(512, 512)



x1 = torch.randn(1, 256)


test_inputs = [other, x1]
