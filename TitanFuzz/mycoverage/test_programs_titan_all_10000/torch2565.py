import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
_input_tensor[1][2] = np.nan
_output_tensor = torch.Tensor.nanmean(_input_tensor, dim=0, keepdim=False)