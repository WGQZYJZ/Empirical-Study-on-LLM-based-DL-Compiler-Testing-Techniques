'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take\ntorch.Tensor.take(_input_tensor, indices)\n'
import torch
input_tensor = torch.arange(0, 10)
indices = torch.tensor([1, 2, 3])
output_tensor = input_tensor.take(indices)
print('input_tensor:', input_tensor)
print('indices:', indices)
print('output_tensor:', output_tensor)