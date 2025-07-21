'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub_\ntorch.Tensor.sub_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.rand(2, 3, dtype=torch.float32)
other = torch.rand(2, 3, dtype=torch.float32)
print('Input tensor: ', input_tensor)
print('Other tensor: ', other)
print('Sub: ', input_tensor.sub_(other))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub\ntorch.Tensor.sub(input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.rand(2, 3, dtype=torch.float32)
other = torch.rand(2, 3, dtype=torch.float32)
print('Input tensor: ', input_tensor)
print('Other tensor: ', other)
print('Sub: ', input_tensor.sub(other))