'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
import torch
input_tensor = torch.randint(10, [2, 3])
print('Input tensor: {}'.format(input_tensor))
cummin_tensor = input_tensor.cummin(dim=0)
print('Cumulative minimum tensor: {}'.format(cummin_tensor))