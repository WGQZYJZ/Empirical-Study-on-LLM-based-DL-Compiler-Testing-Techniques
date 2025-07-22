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



class Model(nn.Module):

    def __init__(self, m0=1.5):
        super().__init__()
        self.a = torch.nn.Parameter(m0)

    def forward(self, input):
        v1 = input.clamp_max(self.a)
        v2 = input.clamp_min(self.a)
        return (v1, v2)




func = Model().to('cuda')



input = torch.randn(1, 1, 64, 64)


test_inputs = [input]
