'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter\ntorch.Tensor.masked_scatter(_input_tensor, mask, tensor)\n'
import torch
input_tensor = torch.rand(3, 4)
mask = torch.tensor([[1, 1, 0, 0], [1, 0, 1, 0], [0, 0, 1, 1]])
tensor = torch.ones(3, 4)
output_tensor = torch.Tensor.masked_scatter(input_tensor, mask, tensor)
print(input_tensor)
print(output_tensor)