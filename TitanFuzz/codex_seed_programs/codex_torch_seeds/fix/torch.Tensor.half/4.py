'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.half\ntorch.Tensor.half(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.randn(1, 3, 224, 224, dtype=torch.float32)
half_tensor = torch.Tensor.half(input_tensor)
print(half_tensor)