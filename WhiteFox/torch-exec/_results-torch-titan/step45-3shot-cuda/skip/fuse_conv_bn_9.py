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
        torch.manual_seed(1)
        self.conv = torch.nn.CBR(2, 2, 1)

    def forward(self, x):
        x = self.conv(x)
        x = self.conv(x)
        return x




func = Model().to('cuda')



x = torch.randn(1, 4, 4, 4)


test_inputs = [x]
