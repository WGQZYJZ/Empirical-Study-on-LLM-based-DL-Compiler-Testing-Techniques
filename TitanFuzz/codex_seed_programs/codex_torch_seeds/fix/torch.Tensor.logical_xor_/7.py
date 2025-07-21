'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor_\ntorch.Tensor.logical_xor_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 0, 0, 1], [0, 1, 1, 0]], dtype=torch.bool)
other = torch.tensor([[1, 1, 0, 0], [0, 1, 0, 0]], dtype=torch.bool)
result = torch.Tensor.logical_xor_(input_tensor, other)
print(result)