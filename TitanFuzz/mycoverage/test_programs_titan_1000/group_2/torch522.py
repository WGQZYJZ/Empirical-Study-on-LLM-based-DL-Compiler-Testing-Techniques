import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=torch.float32)
output_tensor = torch.Tensor.nanquantile(input_tensor, 0.5, dim=None, keepdim=False)