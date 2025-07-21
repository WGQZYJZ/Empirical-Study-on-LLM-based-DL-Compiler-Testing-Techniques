'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arcsinh\ntorch.Tensor.arcsinh(_input_tensor)\n'
import torch
input_tensor = torch.rand(10, 10)
output_tensor = torch.Tensor.arcsinh(input_tensor)
print(output_tensor)