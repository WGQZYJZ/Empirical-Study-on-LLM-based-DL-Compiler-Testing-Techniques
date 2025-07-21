import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([(- 1), (- 2), (- 3), (- 4), (- 5), (- 6), (- 7), (- 8), (- 9), (- 10)])
other = torch.tensor([3, 5, 7, 9, 11, 13, 15, 17, 19, 21])
result = torch.Tensor.bitwise_right_shift_(input_tensor, other)