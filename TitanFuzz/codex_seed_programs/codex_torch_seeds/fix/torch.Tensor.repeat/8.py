'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.repeat\ntorch.Tensor.repeat(_input_tensor, *sizes)\n'
import torch
input_tensor = torch.randint(1, 10, (2, 3))
print('Input tensor:', input_tensor)
output_tensor = input_tensor.repeat(2, 1)
print('Output tensor:', output_tensor)