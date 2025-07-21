'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add_\ntorch.Tensor.add_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[10, 20, 30], [40, 50, 60]])
input_tensor.add_(other)
print(input_tensor)