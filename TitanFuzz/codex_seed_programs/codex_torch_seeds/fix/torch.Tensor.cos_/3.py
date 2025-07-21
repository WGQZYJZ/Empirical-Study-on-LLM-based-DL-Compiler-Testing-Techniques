'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cos_\ntorch.Tensor.cos_(_input_tensor)\n'
import torch
input_tensor = torch.rand(10, dtype=torch.float32)
print('Input Tensor: ', input_tensor)
torch.Tensor.cos_(input_tensor)
print('Output Tensor: ', input_tensor)