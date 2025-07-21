'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.dstack\ntorch.dstack(tensors, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print('input data: ', input_data)
output = torch.dstack((input_data, input_data, input_data))
print('output: ', output)