'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_\ntorch.Tensor.resize_(_input_tensor, *sizes, memory_format=torch.contiguous_format)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('input_tensor: ', input_tensor)
torch.Tensor.resize_(input_tensor, (3, 2, 4))
print('resize_: ', input_tensor)
torch.Tensor.resize_(input_tensor, (3, 2, 4), memory_format=torch.channels_last)
print('resize_: ', input_tensor)