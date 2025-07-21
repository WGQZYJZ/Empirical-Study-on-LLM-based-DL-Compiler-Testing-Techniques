import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
permute_data = torch.permute(input_data, (0, 2, 1))