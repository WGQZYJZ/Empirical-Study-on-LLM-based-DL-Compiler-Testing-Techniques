'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.abs\ntorch.Tensor.abs(_input_tensor)\n'
import torch
input_tensor = torch.randn(10, 3, 4)
output_tensor = input_tensor.abs()
print(output_tensor)