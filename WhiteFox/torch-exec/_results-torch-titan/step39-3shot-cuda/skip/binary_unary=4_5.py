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



class Model():

    def __init__(self):
        pass

    def forward(self, x, other):
        v1 = torch.nn.functional.linear(x, 16)
        v2 = (v1 + other)
        v3 = torch.nn.functional.relu(v2)
        return v3



func = Model().to('cuda')



x = torch.randn(1, 16)



other = torch.randn(1, 16)


test_inputs = [x, other]
