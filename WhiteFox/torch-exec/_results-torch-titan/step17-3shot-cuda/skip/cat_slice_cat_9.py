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
        self.linear1 = torch.nn.Linear()
        self.linear2 = torch.nn.Linear()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:(x3.size(1) + x4.size(1))]
        v4 = torch.cat([v1, v3], dim=1)
        return v4



func = Model().to('cuda')



x1 = torch.randn(1, 2048)



x2 = torch.randn(1, 2048)



x3 = torch.randn(1, 1024)



x4 = torch.randn(1, 1024)


test_inputs = [x1, x2, x3, x4]
