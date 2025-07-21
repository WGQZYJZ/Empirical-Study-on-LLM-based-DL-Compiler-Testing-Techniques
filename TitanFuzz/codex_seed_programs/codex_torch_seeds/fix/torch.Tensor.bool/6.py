'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bool\ntorch.Tensor.bool(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.randn((2, 3, 4), dtype=torch.float32)
bool_tensor = torch.Tensor.bool(input_data)
print('The bool tensor is:\n', bool_tensor)
bool_tensor = torch.Tensor.bool(input_data, memory_format=torch.channels_last)
print('The bool tensor with memory_format is:\n', bool_tensor)