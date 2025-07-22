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

    def __init__(self, m1):
        super().__init__()
        self.m1 = m1

    def forward(self, x1):
        v1 = self.m1(x1)
        o1 = (v1 - other)
        o2 = F.relu(o1)
        return o2




m1 = Model1()

func = Model(m1).to('cuda')



x1 = torch.randn(1, 3, 64, 64)


test_inputs = [x1]
