import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
output_tensor = torch.Tensor.bitwise_not(input_tensor)
input_tensor = torch.rand((3, 3))
output_tensor = torch.Tensor.ceil(input_tensor)