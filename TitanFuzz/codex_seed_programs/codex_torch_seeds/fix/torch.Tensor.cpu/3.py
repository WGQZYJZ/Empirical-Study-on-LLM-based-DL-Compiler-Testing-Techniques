'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cpu\ntorch.Tensor.cpu(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.rand(2, 3, 4, 5)
torch.Tensor.cpu(input_tensor, memory_format=torch.preserve_format)
print('input_tensor: ', input_tensor)
print('input_tensor.device: ', input_tensor.device)
print('input_tensor.dtype: ', input_tensor.dtype)
print('input_tensor.layout: ', input_tensor.layout)
print('input_tensor.shape: ', input_tensor.shape)
print('input_tensor.stride(): ', input_tensor.stride())
print('input_tensor.numel(): ', input_tensor.numel())
print('input_tensor.size(): ', input_tensor.size())
print('input_tensor.dim(): ', input_tensor.dim())