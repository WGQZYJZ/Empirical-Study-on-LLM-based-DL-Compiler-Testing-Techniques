import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]], dtype=torch.uint8)
torch.Tensor.bitwise_left_shift(_input_tensor, 2)