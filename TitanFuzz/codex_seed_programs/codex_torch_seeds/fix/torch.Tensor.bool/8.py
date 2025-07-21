'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bool\ntorch.Tensor.bool(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('Input tensor:', input_tensor)
bool_tensor = input_tensor.bool()
print('Bool tensor:', bool_tensor)
bool_tensor = input_tensor.bool(memory_format=torch.channels_last)
print('Bool tensor:', bool_tensor)