import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.int32)
output_tensor = torch.Tensor.bitwise_not_(input_tensor)
output_tensor = torch.bitwise_not(input_tensor)