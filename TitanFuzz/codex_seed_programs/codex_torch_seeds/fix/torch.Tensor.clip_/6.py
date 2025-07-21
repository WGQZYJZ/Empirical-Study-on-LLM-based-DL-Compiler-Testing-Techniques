'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clip_\ntorch.Tensor.clip_(_input_tensor, min=None, max=None)\n'
import torch
input_tensor = torch.arange(1, 11, dtype=torch.float32)
print('Input Tensor: \n', input_tensor)
output_tensor = torch.Tensor.clip_(input_tensor, min=3, max=7)
print('Output Tensor: \n', output_tensor)