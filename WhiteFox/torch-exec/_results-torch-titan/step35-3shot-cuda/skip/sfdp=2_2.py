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



dim = 128


seq_length = 256


batch_size = 1


query = torch.randn(batch_size, seq_length, dim)



dim = 128


seq_length = 256


batch_size = 1


key = torch.randn(batch_size, seq_length, dim)




seq_length = 256


seq_length = 256


query = torch.randn(batch_size, seq_length, dim)


query = torch.randn(batch_size, seq_length, dim)



mask = torch.logical_or((torch.arange(seq_length).to(query.device) > 250), (torch.arange(seq_length).to(query.device) < 100))


test_inputs = [query, key, mask]
