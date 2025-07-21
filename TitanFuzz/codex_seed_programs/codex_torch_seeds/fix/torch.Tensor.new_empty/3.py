'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.new_empty\ntorch.Tensor.new_empty(_input_tensor, size, dtype=None, device=None, requires_grad=False)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
new_empty_tensor = torch.Tensor.new_empty(input_tensor, (2, 3))
print(new_empty_tensor)