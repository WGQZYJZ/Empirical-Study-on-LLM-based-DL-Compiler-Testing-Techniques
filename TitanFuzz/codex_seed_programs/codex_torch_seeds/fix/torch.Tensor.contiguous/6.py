'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.contiguous\ntorch.Tensor.contiguous(_input_tensor, memory_format=torch.contiguous_format)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print(input_tensor)
output_tensor = input_tensor.contiguous(memory_format=torch.channels_last)
print(output_tensor)