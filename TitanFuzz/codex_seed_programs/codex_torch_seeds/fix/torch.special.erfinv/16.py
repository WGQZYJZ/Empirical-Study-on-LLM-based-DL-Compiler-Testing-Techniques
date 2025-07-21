'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.erfinv\ntorch.special.erfinv(input, *, out=None)\n'
import torch
input_data = torch.randn(1, requires_grad=True)
print('Input data: ', input_data)
output = torch.special.erfinv(input_data)
print('Output: ', output)