import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3, 5)
torch.nn.LayerNorm(normalized_shape=1, eps=1e-05, elementwise_affine=True, device=None, dtype=None)