'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract\ntorch.Tensor.subtract(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other_tensor = torch.tensor([[1, 1, 1], [1, 1, 1]])
print('input_tensor:')
print(input_tensor)
print('other_tensor:')
print(other_tensor)
print('torch.Tensor.subtract(input_tensor, other_tensor):')
print(torch.Tensor.subtract(input_tensor, other_tensor))
print('torch.Tensor.subtract(input_tensor, other_tensor, alpha=2):')
print(torch.Tensor.subtract(input_tensor, other_tensor, alpha=2))