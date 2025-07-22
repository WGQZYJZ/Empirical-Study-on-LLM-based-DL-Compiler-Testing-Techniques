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

    def forward(self, x1):
        x2 = x1.flatten().reshape((- 1), 400000000)
        x3 = x2[:, 0:2147483648]
        x4 = x2[:, 0:5368709120]
        x5 = torch.concatenate([x2, x4], dim=1)
        return x5



func = Model().to('cuda')

x1 = 1

test_inputs = [x1]
