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



class m1(torch.nn.Module):

    def __init__(self, m2):
        super().__init__()

    def forward(self, x1):
        x2 = x1
        x3 = torch.nn.functional.dropout(x1)
        x4 = self.m2(x2)
        return torch.nn.functional.dropout(x3)




class m2(torch.nn.Module):

    def forward(self, x1):
        x2 = x1
        x3 = torch.nn.functional.dropout(x2)
        return x3



m2 = 1

func = m2(m2).to('cuda')



x1 = torch.randn(1, 2, 2)


test_inputs = [x1]
