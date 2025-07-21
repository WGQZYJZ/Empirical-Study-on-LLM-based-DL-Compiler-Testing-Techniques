'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool1d\ntorch.nn.AdaptiveMaxPool1d(output_size, return_indices=False)\n'
import torch
from torch.autograd import Variable
from torch.nn.parameter import Parameter
import torch
input = Variable(torch.Tensor([[[1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9]]]))
pool = torch.nn.AdaptiveMaxPool1d(3)
output = pool(input)
print(output)