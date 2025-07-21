'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sqrt\ntorch.Tensor.sqrt(_input_tensor)\n'
import torch
input_tensor = torch.randn(10, 20)
output_tensor = torch.Tensor.sqrt(input_tensor)
print(output_tensor)