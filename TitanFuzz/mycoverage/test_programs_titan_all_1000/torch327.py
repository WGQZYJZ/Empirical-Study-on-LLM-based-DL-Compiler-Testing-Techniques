import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(12, dtype=torch.float32).reshape(3, 4)
output_tensor = torch.Tensor.broadcast_to(input_tensor, (2, 3, 4))