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
        self.cat3 = torch.cat((None, None), dim=(- 1))

    def forward(self, x):
        x = torch.cat((x, x), dim=(- 1))
        x = x.view(x.shape[0], (- 1))
        return x




func = Model().to('cuda')



x = torch.randn(2, 3, 4)


test_inputs = [x]
