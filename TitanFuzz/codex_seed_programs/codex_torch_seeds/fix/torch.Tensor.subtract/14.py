'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract\ntorch.Tensor.subtract(_input_tensor, other, *, alpha=1)\n'
import torch
import torch
input_tensor = torch.rand(2, 3)
other = torch.rand(2, 3)
output_tensor = torch.Tensor.subtract(input_tensor, other, alpha=1)
print(output_tensor)