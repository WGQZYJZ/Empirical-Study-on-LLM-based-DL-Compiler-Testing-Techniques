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

    def forward(self, x1, x2, x1, x2, x1, x2, x3, x4, x1, y1, y2):
        b1 = torch.matmul(x1, x2)
        b2 = torch.sigmoid(x3)
        c = b1 + b2
        d = c + x4
        e = torch.sigmoid(d)
        y = torch.matmul(y1, y2)
        return e + y + y1 + y2



func = Model().to('cpu')


x1 = torch.randn(3, 3)

x2 = torch.randn(3, 3)

x3 = torch.randn(3, 3)

x4 = torch.randn(3, 3)

y1 = torch.randn(3, 3)

y2 = torch.randn(3, 3)

test_inputs = [x1, x2, x3, x4, y1, y2]
