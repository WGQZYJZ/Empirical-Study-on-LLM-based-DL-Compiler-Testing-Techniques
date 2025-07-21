'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros\ntorch.zeros(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.tensor([[1, 2], [3, 4]])
output_data = torch.zeros(input_data.size())
print('Input data: ', input_data)
print('Output data: ', output_data)