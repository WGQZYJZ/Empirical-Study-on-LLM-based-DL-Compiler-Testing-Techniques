'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erfc\ntorch.erfc(input, *, out=None)\n'
import torch
data = torch.randn(3, 4)
print('Input data: ', data)
output = torch.erfc(data)
print('Output data: ', output)