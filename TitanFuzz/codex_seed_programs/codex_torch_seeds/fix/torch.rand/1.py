'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rand\ntorch.rand(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.rand(1, 3)
print('input_data is: ', input_data)
weights = torch.rand(3, 1)
print('weights is: ', weights)
output = torch.mm(input_data, weights)
print('output is: ', output)