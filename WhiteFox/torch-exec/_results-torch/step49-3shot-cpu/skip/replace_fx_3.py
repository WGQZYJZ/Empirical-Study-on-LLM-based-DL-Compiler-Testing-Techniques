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

class Model(torch.nn.module.Module):

    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = F.dropout(x, p=0.1, training=True)
        x = torch.rand_like(x)
        x = F.dropout(x, p=0.5)
        x = F.dropout(x, p=0.5)
        return x



func = Model().to('cpu')


x1 = torch.randn(1, 2, 2)

test_inputs = [x1]
