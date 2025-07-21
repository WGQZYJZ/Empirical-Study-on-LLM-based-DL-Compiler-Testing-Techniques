'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(5, 5))
print('Input tensor: \n{}'.format(input_tensor))
cummin = input_tensor.cummin(dim=1)
print('\nCummin: \n{}'.format(cummin))