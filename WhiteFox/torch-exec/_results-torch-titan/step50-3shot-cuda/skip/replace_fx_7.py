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



class network(torch.nn.Module):

    def __init__(self):
        super().__init__()
        torch.nn.init.constant_(self.v1.weight, val=0.5)

    def forward(self, x):
        out = F.dropout(x)
        self.v1(out)
        return out




func = network().to('cuda')



x1 = torch.randn(32, 32)


test_inputs = [x1]
