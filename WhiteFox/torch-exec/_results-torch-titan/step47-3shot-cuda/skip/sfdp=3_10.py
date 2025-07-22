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



func = ().to('cuda')



_query = torch.randn(2, 4, 10)



_key = torch.randn(2, 10, 20)



_value = torch.randn(2, 10, 20)


test_inputs = [_query, _key, _value]
