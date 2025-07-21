import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
layer_norm = torch.nn.LayerNorm([4], eps=1e-05, elementwise_affine=True)