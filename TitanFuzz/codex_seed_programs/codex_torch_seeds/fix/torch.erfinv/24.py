'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erfinv\ntorch.erfinv(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3)
print('Input Data: ', input_data)
output = torch.erfinv(input_data)
print('Output: ', output)