'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow\ntorch.Tensor.narrow(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.randint(0, 10, (3, 4, 5))
print('Input tensor:', input_tensor)
output_tensor = input_tensor.narrow(1, 1, 2)
print('Output tensor:', output_tensor)