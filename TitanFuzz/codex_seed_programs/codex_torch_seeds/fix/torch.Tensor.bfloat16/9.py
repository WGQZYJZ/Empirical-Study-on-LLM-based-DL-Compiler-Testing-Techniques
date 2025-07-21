'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bfloat16\ntorch.Tensor.bfloat16(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.rand(4, 4)
print(input_tensor)
bfloat16_tensor = torch.Tensor.bfloat16(input_tensor)
print(bfloat16_tensor)