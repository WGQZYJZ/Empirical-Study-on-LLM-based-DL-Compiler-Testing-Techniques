'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros\ntorch.zeros(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = [1, 2, 3, 4, 5]
x = torch.tensor(input_data)
print('Input data: ', x)
print('Size of input data: ', x.shape)
y = torch.zeros(5, dtype=torch.long)
print('Output data: ', y)
print('Size of output data: ', y.shape)