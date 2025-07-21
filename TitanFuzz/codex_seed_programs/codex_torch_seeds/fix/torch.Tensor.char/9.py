'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.char\ntorch.Tensor.char(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.randn(4, 3, 32, 32)
print(torch.is_tensor(input_tensor))
print(torch.is_storage(input_tensor))
print(torch.numel(input_tensor))
print(torch.Tensor.char(input_tensor))
print(torch.Tensor.char(input_tensor, memory_format=torch.channels_last))