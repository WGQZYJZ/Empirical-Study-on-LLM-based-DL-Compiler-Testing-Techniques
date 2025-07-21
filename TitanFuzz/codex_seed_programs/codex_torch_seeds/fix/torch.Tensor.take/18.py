'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take\ntorch.Tensor.take(_input_tensor, indices)\n'
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor)
indices = torch.tensor([0, 2])
output_tensor = input_tensor.take(indices)
print(output_tensor)