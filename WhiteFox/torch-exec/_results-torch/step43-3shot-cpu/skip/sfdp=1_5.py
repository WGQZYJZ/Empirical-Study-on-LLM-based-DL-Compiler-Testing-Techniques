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
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, x, y):
        a = torch.matmul(x, y.transpose(-2, -1))
        b = a / inv_scale_factor
        c = torch.nn.functional.dropout(b.softmax(dim=-1), self.dropout_p)
        d = torch.matmul(c, z)
        return d


func = Model().to('cpu')

x = 1
y = 1

test_inputs = [x, y]
