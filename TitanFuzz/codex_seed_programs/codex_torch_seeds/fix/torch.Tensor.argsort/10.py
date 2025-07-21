'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argsort\ntorch.Tensor.argsort(_input_tensor, dim=-1, descending=False)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
_sorted_tensor = _input_tensor.argsort(dim=(- 1), descending=False)
print(_sorted_tensor)
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.Tensor.argsort')
print('torch.Tensor.argsort(_input_tensor, dim=-1, descending=False)')
print('_sorted_tensor = _input_tensor.argsort(dim=-1, descending=False)')