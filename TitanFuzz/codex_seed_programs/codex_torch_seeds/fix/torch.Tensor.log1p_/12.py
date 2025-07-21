'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log1p_\ntorch.Tensor.log1p_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
output_tensor = torch.log1p(input_tensor)
print(output_tensor)
output_tensor = torch.Tensor.log1p_(input_tensor)
print(output_tensor)