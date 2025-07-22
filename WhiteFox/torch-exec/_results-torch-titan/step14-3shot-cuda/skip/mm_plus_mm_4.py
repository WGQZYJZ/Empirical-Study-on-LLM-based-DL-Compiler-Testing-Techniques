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

    def forward(x):
        x = (x + 1)
        return x
    return self.forward(input)




func = Model().to('cuda')

input_tensor = torch.randn(1, 1, 1)

test_inputs = [input_tensor]
