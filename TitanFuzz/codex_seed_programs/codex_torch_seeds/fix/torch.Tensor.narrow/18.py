'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow\ntorch.Tensor.narrow(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.randn(1, 3, 3)
print(input_tensor)
output_tensor = input_tensor.narrow(1, 0, 2)
print(output_tensor)