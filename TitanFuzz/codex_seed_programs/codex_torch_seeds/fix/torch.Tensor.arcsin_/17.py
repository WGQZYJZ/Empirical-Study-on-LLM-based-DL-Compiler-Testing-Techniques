'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arcsin_\ntorch.Tensor.arcsin_(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
output_tensor = torch.Tensor.arcsin_(input_tensor)
print(output_tensor)