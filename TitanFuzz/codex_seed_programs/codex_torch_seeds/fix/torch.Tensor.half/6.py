'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.half\ntorch.Tensor.half(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import torch
input_tensor = torch.randn(3, 3, dtype=torch.float32)
output_tensor = torch.Tensor.half(input_tensor)
print(output_tensor)