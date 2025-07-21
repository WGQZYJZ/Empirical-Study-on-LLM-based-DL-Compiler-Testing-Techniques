'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_select\ntorch.Tensor.masked_select(_input_tensor, mask)\n'
import torch
import torch
input_tensor = torch.randn(10, 10)
mask = torch.rand(10, 10)
output_tensor = torch.Tensor.masked_select(input_tensor, mask)
print(output_tensor)