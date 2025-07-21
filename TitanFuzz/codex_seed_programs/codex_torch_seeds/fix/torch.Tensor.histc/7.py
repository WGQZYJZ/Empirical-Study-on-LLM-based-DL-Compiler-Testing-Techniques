'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.histc\ntorch.Tensor.histc(_input_tensor, bins=100, min=0, max=0)\n'
import torch
input_tensor = torch.rand(100)
output_tensor = torch.Tensor.histc(input_tensor, bins=100, min=0, max=1)
print(output_tensor)