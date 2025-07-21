import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([0, 1, 1, 0], dtype=torch.float32)
other_data = torch.tensor([1, 0, 1, 0], dtype=torch.float32)
result = torch.not_equal(input_data, other_data)