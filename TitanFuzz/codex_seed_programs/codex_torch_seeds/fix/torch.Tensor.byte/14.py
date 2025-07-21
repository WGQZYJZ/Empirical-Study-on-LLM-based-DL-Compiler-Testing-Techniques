'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.byte\ntorch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.rand(3, 3)
output_tensor = torch.Tensor.byte(input_tensor, memory_format=torch.preserve_format)
print(output_tensor)