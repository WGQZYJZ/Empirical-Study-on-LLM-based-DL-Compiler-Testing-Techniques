import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.int32)
bitwise_right_shift_ = torch.Tensor.bitwise_right_shift_(input_tensor, other=2)