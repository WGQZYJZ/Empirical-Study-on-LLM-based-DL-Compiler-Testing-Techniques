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
        pass

    def forward(self, t1, t2, size):
        t3 = t1[:, 0:size]
        t4 = torch.cat([t1, t3], dim=1)
        return t4



func = Model().to('cuda')



x1 = torch.randn(1, 2, 32, 32)



x2 = torch.randn(1, 3, 32, 32)

t1 = 1

test_inputs = [x1, x2, t1]
