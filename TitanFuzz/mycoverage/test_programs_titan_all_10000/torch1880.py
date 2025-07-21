import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
other = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
output_tensor = torch.Tensor.less_(input_tensor, other)