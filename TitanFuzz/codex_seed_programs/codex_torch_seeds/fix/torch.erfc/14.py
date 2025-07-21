'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erfc\ntorch.erfc(input, *, out=None)\n'
import torch
in_data = torch.randn(4, 4)
print('Input data is: ', in_data)
out_data = torch.erfc(in_data)
print('Output data is: ', out_data)