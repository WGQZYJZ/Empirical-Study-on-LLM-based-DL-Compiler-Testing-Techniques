'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor_\ntorch.Tensor.logical_xor_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 1]])
other = torch.tensor([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 1]])
print(input_tensor.logical_xor_(other))
'\nTask 4: Call the API torch.Tensor.logical_xor\ntorch.Tensor.logical_xor(other)\n'
print(input_tensor.logical_xor(other))