import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3, 4], [4, 3, 2, 1]])
flipped_data = torch.flip(input_data, dims=[0])