'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow\ntorch.Tensor.narrow(_input_tensor, dimension, start, length)\n'
import torch
input_tensor = torch.arange(0, 12, dtype=torch.float32).reshape(4, 3)
print('input_tensor: {}'.format(input_tensor))
output_tensor = torch.Tensor.narrow(input_tensor, dimension=0, start=1, length=2)
print('output_tensor: {}'.format(output_tensor))