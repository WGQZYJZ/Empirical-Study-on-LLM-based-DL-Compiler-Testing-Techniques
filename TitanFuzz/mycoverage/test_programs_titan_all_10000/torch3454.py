import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.float32)
output_tensor = torch.Tensor.bitwise_left_shift(input_tensor, 2)