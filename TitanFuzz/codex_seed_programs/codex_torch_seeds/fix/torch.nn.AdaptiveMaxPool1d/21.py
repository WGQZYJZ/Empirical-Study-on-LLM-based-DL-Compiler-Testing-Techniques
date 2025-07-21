'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.Tensor([[[1, 2, 3, 4, 5, 6, 7]]]))
maxpool = torch.nn.AdaptiveMaxPool1d(3)
output = maxpool(input)
print(output)