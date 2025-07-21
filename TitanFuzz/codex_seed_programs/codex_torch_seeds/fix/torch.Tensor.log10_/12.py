'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log10_\ntorch.Tensor.log10_(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 4, 5)
output_tensor = torch.Tensor.log10_(input_tensor)
print(input_tensor)
print(output_tensor)