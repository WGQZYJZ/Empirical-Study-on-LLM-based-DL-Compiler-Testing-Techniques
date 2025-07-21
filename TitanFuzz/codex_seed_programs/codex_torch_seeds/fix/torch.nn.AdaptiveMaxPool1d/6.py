'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = Variable(torch.randn(1, 1, 4))
print(x)
torch.nn.AdaptiveMaxPool1d(1, return_indices=False)
print(torch.nn.AdaptiveMaxPool1d(1, return_indices=False)(x))