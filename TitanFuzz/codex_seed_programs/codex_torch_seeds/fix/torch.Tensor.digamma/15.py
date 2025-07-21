'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.digamma\ntorch.Tensor.digamma(_input_tensor)\n'
import torch
input_tensor = torch.rand(10)
print(input_tensor)
output_tensor = torch.Tensor.digamma(input_tensor)
print(output_tensor)