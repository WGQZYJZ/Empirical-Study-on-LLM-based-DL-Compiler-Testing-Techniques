'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow\ntorch.Tensor.narrow(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.arange(1, 11, dtype=torch.float32)
print('input_tensor: ', input_tensor)
output_tensor = torch.Tensor.narrow(input_tensor, 0, 2, 5)
print('output_tensor: ', output_tensor)