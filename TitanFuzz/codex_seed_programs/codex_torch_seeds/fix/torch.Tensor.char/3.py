'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.char\ntorch.Tensor.char(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
print('input_tensor:', input_tensor)
output_tensor = input_tensor.char()
print('output_tensor:', output_tensor)