'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rsqrt\ntorch.Tensor.rsqrt(_input_tensor)\n'
import torch
input_tensor = torch.randn(1)
print(input_tensor)
output_tensor = input_tensor.rsqrt()
print(output_tensor)