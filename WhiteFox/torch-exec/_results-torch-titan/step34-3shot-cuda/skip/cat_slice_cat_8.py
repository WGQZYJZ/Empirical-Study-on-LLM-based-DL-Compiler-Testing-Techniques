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

    def __init__(self, size=256):
        super().__init__()

    def forward(self, *x):
        t1 = torch.cat(x, dim=1)
        tmp = int(t1.shape[1])
        t2 = t1[:, 0:tmp]
        tmp2 = int(t2.shape[1])
        st1 = t2[:, 0:self.size]
        t3 = torch.cat([t1, st1], dim=1)
        return t3



func = Model(size=size).to('cuda')



x1 = torch.randn(1, 3, 64, 64)



x2 = torch.randn(1, 3, 64, 64)


test_inputs = [x1, x2]
