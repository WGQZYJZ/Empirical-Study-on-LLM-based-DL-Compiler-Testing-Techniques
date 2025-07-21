import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(2, 3, dtype=torch.float32)
output_data = torch.conj_physical(input_data)