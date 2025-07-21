'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erfinv\ntorch.erfinv(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 2, 3)
output = torch.erfinv(input_data)
print('Input: ', input_data)
print('Output: ', output)