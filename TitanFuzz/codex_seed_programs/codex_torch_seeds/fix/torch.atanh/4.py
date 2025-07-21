'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atanh\ntorch.atanh(input, *, out=None)\n'
import torch
import torch
data = torch.randn(1, 1)
print('The input data is: ', data)
output = torch.atanh(data)
print('The output is: ', output)