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

    def __init__(self, output_w, output_h, channels, other):
        super().__init__()
        self.linear1 = torch.nn.Linear(channels, 3)
        self.linear2 = torch.nn.Linear(((output_w * output_h) * 3), 1)
        self.other = other

    def forward(self, x):
        v1 = self.linear1(x)
        v2 = (v1 + self.other)
        v3 = self.linear2(v2)
        return torch.sigmoid(v3)



output_w = 1
output_h = 1

channels = 3


other = torch.randn(1, 3, 64, 64)

func = Model(w, h, channels, other).to('cuda')



other = torch.randn(1, 3, 64, 64)



h = 64


w = 64


channels = 3


x = torch.randn(1, channels, w, h)


test_inputs = [other, x]
