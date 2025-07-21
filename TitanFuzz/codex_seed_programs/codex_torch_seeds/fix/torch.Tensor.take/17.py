'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take\ntorch.Tensor.take(_input_tensor, indices)\n'
import torch
import torch
input_tensor = torch.arange(0, 10)
print('input_tensor:', input_tensor)
indices = torch.tensor([3, 1, 2, 4])
output_tensor = input_tensor.take(indices)
print('output_tensor:', output_tensor)