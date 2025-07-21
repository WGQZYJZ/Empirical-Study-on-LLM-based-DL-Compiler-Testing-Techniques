'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expm1\ntorch.Tensor.expm1(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.expm1(input_tensor)
print(output_tensor)