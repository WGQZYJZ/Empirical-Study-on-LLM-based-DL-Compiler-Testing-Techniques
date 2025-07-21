import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.int32)
torch.Tensor.bitwise_left_shift_(input_tensor, other=2)