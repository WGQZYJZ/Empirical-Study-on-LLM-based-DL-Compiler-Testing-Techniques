'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.long\ntorch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print(input_tensor)
output_tensor = torch.Tensor.long(input_tensor, memory_format=torch.preserve_format)
print(output_tensor)