import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
output_tensor = torch.Tensor.bitwise_left_shift_(input_tensor, 2)