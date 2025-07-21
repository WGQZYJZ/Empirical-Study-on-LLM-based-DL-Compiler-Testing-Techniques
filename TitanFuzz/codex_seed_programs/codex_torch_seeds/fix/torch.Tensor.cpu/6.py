'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cpu\ntorch.Tensor.cpu(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import torch
input_tensor = torch.randn(2, 3, 4, 5, 6)
output_tensor = input_tensor.cpu(memory_format=torch.preserve_format)
print(input_tensor)
print(output_tensor)