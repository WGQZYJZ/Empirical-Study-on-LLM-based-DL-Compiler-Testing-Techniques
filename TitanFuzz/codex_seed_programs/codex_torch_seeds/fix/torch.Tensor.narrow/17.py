'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow\ntorch.Tensor.narrow(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.randn(5, 3)
print(input_tensor)
output_tensor = torch.Tensor.narrow(input_tensor, 1, 0, 2)
print(output_tensor)