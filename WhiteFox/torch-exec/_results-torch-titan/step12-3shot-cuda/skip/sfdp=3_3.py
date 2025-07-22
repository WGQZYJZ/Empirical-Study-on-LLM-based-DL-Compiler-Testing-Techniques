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
        self.linear1 = torch.nn.Linear(16, 16, stride=1, padding=1)
        self.dropout = torch.nn.Dropout(0.5)
        self.linear2 = torch.nn.Linear(16, 16, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.linear1(x1)
        v2 = self.dropout(v1)
        v3 = self.linear2(v2)
        v4 = torch.matmul(v3, x2.transpose((- 2), (- 1)))
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 16, 16, 16)



x2 = torch.randn(1, 64, 40)


test_inputs = [x1, x2]
