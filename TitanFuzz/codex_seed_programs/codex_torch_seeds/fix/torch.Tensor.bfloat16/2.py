'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bfloat16\ntorch.Tensor.bfloat16(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
x = torch.rand(3, 3, dtype=torch.float32)
print('Input data: ', x)
y = torch.Tensor.bfloat16(x)
print('Output data: ', y)