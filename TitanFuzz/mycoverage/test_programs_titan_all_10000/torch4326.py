import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.arange(0, 12, dtype=torch.float32).reshape(2, 3, 2)
output_tensor = torch.Tensor.as_strided(input_tensor, size=(2, 2, 2), stride=(2, 2, 2))