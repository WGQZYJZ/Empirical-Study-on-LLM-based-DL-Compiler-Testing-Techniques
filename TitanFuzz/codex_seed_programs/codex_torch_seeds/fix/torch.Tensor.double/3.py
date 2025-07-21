'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.double\ntorch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.randn(4, 4)
doubled_tensor = torch.Tensor.double(input_tensor, memory_format=torch.preserve_format)
print(doubled_tensor)