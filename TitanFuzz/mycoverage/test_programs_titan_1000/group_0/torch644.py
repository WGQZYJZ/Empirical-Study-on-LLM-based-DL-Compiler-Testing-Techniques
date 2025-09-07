import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([1, 2, 3, 4], dtype=torch.int32)
result = torch.Tensor.bitwise_left_shift(input_tensor, 2)