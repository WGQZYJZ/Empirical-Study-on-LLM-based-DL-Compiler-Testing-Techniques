'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.half\ntorch.Tensor.half(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.rand(3, 3)
output_tensor = torch.Tensor.half(input_tensor)
print(input_tensor)
print(output_tensor)