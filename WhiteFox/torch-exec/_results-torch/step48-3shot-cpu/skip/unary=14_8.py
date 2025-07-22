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

class toto(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.pad = torch.nn.functional.pad(torch.empty(507904, 768, 26, 26, dtype=torch.float), (26, 26, 26, 26), value=0.0)

    def forward(self, x):
        v1 = self.pad(x)
        return v1



func = toto().to('cpu')


x1 = torch.randn(1, 59712, 56, 56)

x2 = torch.randn(1, 768, 26, 26)

test_inputs = [x1, x2]
