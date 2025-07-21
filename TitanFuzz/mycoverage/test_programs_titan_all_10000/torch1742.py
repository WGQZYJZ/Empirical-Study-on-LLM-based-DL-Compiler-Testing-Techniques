import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.arange(1, 17, dtype=torch.float32).reshape(4, 4)
reps = (2, 1)
output = torch.tile(input_data, reps)