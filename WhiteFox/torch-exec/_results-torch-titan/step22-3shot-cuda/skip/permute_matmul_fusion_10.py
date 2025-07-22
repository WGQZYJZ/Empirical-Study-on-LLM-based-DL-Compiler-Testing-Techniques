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
        self.permute = torch.nn.functional.permute

    def forward(self, x1, x2):
        v1 = self.permute(x1, (0, 2, 1))
        return self.permute(torch.matmul(x2, v1), (0, 2, 1))




func = Model().to('cuda')



x1 = torch.randn(1, 2, 2)



x2 = torch.randn(1, 2, 2)


test_inputs = [x1, x2]
