'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_max_pool3d\ntorch.nn.functional.adaptive_max_pool3d(input, output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 10, 10, 10))
output_size = (2, 3, 4)
torch.nn.functional.adaptive_max_pool3d(input, output_size, return_indices=False)