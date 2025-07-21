'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take\ntorch.Tensor.take(_input_tensor, indices)\n'
import torch
input_tensor = torch.arange(0, 12).reshape(3, 4)
print('input tensor:', input_tensor)
indices = torch.tensor([0, 2])
output_tensor = input_tensor.take(indices)
print('output tensor:', output_tensor)