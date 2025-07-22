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
        self.cat1 = torch.nn.Parameter(torch.full([10, 641, 7], 1, dtype=torch.int64))
        self.cat2 = torch.nn.Parameter(torch.full([10, 128, 7], 1, dtype=torch.int64))

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, (- 1):]
        v3 = v2[:, :x1.size()[1]]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')



x1 = torch.randint(1, 10, [3, 640, 7])



x2 = torch.randint(1, 10, [3, 128, 7])


test_inputs = [x1, x2]
