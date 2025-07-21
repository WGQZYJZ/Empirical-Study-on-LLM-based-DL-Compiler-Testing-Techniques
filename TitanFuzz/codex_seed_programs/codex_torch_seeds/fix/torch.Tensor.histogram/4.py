'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histogram\ntorch.Tensor.histogram(_input_tensor, input, bins, *, range=None, weight=None, density=False)\n'
import torch
_input_tensor = torch.randint(low=0, high=10, size=(10,))
print('Input tensor: {}'.format(_input_tensor))
hist_without_range = torch.Tensor.histogram(_input_tensor, bins=10)
print('histogram without parameter range: {}'.format(hist_without_range))
hist_with_range = torch.Tensor.histogram(_input_tensor, bins=10, range=(0, 10))
print('histogram with parameter range: {}'.format(hist_with_range))