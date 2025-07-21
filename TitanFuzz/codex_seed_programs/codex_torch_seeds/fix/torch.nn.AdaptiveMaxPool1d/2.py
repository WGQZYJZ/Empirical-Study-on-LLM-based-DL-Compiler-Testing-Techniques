'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch
input = torch.randn(1, 1, 4)
max_pooling = torch.nn.AdaptiveMaxPool1d(1)
output = max_pooling(Variable(input))
print(output)