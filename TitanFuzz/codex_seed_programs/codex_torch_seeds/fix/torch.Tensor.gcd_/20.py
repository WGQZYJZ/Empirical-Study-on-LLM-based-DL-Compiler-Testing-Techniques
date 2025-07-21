'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd_\ntorch.Tensor.gcd_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[7, 8, 9], [10, 11, 12]])
input_tensor.gcd_(other)
print('input_tensor:', input_tensor)