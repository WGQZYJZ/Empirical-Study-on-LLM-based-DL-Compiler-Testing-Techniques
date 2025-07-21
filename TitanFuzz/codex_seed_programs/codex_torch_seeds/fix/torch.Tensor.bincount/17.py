'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bincount\ntorch.Tensor.bincount(_input_tensor, weights=None, minlength=0)\n'
import torch
input_tensor = torch.Tensor([[0, 1, 1, 2], [1, 1, 1, 2]])
print('input_tensor: ', input_tensor)
counts = input_tensor.bincount()
print('counts: ', counts)
counts = input_tensor.bincount(minlength=5)
print('counts: ', counts)
counts = input_tensor.bincount(weights=torch.Tensor([1, 2]))
print('counts: ', counts)
counts = input_tensor.bincount(weights=torch.Tensor([[1, 2], [3, 4]]))
print('counts: ', counts)