'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.geqrf\ntorch.geqrf(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 5)
print('Input data: ', input_data)
output = torch.geqrf(input_data)
print('Output of torch.geqrf: ', output)