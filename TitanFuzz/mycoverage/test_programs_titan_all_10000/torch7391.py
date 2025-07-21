import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, float('nan')], [4, float('nan'), 6], [float('nan'), 8, 9]])
output_tensor = torch.Tensor.nan_to_num(input_tensor)