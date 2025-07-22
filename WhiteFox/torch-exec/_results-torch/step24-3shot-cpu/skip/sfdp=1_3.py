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

    def forward(self, x1, x2):
        x3 = x2.transpose(-2, -1)
        v1 = torch.matmul(x1, x3)
        v2 = v1 / 0.06928203230275509
        v3 = v2.softmax(-1)
        v4 = F.dropout(v3, p=0.05)
        v5 = torch.matmul(v4, x2)
        return v5


func = Model().to('cpu')


x1 = torch.ones(1, 3, 5)

x2 = torch.ones(1, 5, 2)

test_inputs = [x1, x2]
