'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igamma_\ntorch.Tensor.igamma_(_input_tensor, other)\n'
import torch
from torch.autograd import Variable
import torch
input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
torch.Tensor.igamma_(input_tensor, other)