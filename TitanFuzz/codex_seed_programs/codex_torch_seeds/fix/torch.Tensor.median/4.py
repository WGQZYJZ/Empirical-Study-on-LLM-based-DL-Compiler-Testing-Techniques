'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.median\ntorch.Tensor.median(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randint(low=0, high=10, size=(2, 3))
print('Input tensor: {}'.format(_input_tensor))
_median = torch.Tensor.median(_input_tensor)
print('Median: {}'.format(_median))