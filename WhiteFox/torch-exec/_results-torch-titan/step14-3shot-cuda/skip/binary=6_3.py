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

    def __init__():
        super().__init__()
        self.fc = torch.nn.Linear(100, 100)

    def forward(self, x):
        v1 = self.fc(x)
        return (v1 - 5)



func = Model().to('cuda')



x1 = torch.randn(1, 100)


test_inputs = [x1]
