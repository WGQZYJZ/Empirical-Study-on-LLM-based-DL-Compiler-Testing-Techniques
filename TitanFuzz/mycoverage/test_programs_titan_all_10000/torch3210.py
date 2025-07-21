import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
input_tensor[(1, 1)] = torch.nan
mean_value = torch.Tensor.nanmean(input_tensor)
mean_value = torch.Tensor.nanmean(input_tensor, dim=0)
mean_value = torch.Tensor.nanmean(input_tensor, dim=1)