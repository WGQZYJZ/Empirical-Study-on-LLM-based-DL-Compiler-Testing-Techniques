'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log10\ntorch.Tensor.log10(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
output_tensor = torch.Tensor.log10(input_tensor)
print(output_tensor)